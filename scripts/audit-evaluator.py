#!/usr/bin/env python3
import json
import logging
import os
import subprocess
import sys
import urllib.error
import urllib.request
from collections import OrderedDict
from typing import Dict, List, Optional
from urllib.parse import quote, urljoin, urlparse

import yaml

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
AUDIT = os.path.join(ROOT, "audit")
GITHUB_API_URL = os.environ.get("GITHUB_API_URL", "https://api.github.com")

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")


def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def file_contains(path, substrings):
    try:
        with open(
            os.path.join(ROOT, path), "r", encoding="utf-8", errors="ignore"
        ) as f:
            text = f.read()
        return all(s in text for s in substrings)
    except FileNotFoundError:
        return False


def path_exists(all_paths):
    return all(os.path.exists(os.path.join(ROOT, p)) for p in all_paths)


def score_rules(rules):
    score = 0
    breakdown = []
    for name, rule in rules.items():
        ok = True
        if "file" in rule and "must_contain" in rule:
            ok = file_contains(rule["file"], rule["must_contain"])
        if "path_exists" in rule:
            ok = ok and path_exists(rule["path_exists"])
        pts = rule.get("weight", 1) if ok else 0
        score += pts
        breakdown.append({"rule": name, "ok": ok, "weight": rule.get("weight", 1)})
    return score, breakdown


def summarize_audit_inputs():
    personas = scenarios = impacts = 0
    for sub in ("personas", "escenarios", "impactos"):
        directory = os.path.join(AUDIT, sub)
        if os.path.isdir(directory):
            count = sum(
                1 for f in os.listdir(directory) if f.endswith((".yml", ".yaml"))
            )
            if sub == "personas":
                personas = count
            if sub == "escenarios":
                scenarios = count
            if sub == "impactos":
                impacts = count
    return {"personas": personas, "scenarios": scenarios, "impacts": impacts}


def _summarize_failures(summary):
    """Build a terse rationale based on the deterministic audit results."""

    breakdown = summary.get("breakdown", [])
    failed_rules = [
        item.get("rule", "unknown") for item in breakdown if not item.get("ok", False)
    ]

    if summary.get("passed"):
        return (
            f"Score {summary.get('score')} meets the pass threshold "
            f"of {summary.get('pass_score')}"
            + (
                ". All required rules passed."
                if not failed_rules
                else ". Minor rule deviations detected but overall score passed."
            )
        )

    if failed_rules:
        failures = ", ".join(failed_rules[:5])
        if len(failed_rules) > 5:
            failures += ", …"
        return (
            f"Score {summary.get('score')} below pass threshold "
            f"{summary.get('pass_score')}. Failing rules: {failures}."
        )

    return (
        f"Score {summary.get('score')} below pass threshold {summary.get('pass_score')}"
    )


def _llm_payload(summary, endpoint="chat"):
    model = os.environ.get("LLM_MODEL", "DeepSeek-R1-Distill-Qwen-14B-W4A16")
    system_prompt = (
        "You are assisting with an internal audit. Given the JSON summary of the "
        "automated checks, return a short JSON object with the fields 'status' "
        "(values: PASS or FAIL) and 'rationale' (a concise explanation)."
    )
    summary_text = json.dumps(summary, ensure_ascii=False)
    if endpoint == "responses":
        return {
            "model": model,
            "input": [
                {
                    "role": "system",
                    "content": [{"type": "text", "text": system_prompt}],
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": (
                                "Audit summary:\n"
                                + summary_text
                                + "\nRespond only with JSON."
                            ),
                        }
                    ],
                },
            ],
            "temperature": 0.1,
            "max_output_tokens": 200,
        }

    return {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {
                "role": "user",
                "content": (
                    "Audit summary:\n" + summary_text + "\nRespond only with JSON."
                ),
            },
        ],
        "temperature": 0.1,
        "max_tokens": 200,
    }


def _join_url(base, path):
    """Helper to safely append a path segment to the provided base URL."""

    return urljoin(base.rstrip("/") + "/", path.lstrip("/"))


def _expand_candidate(seed):
    """Return candidate URLs inferred from the provided seed value."""

    if not seed:
        return []

    seed = seed.strip()
    if not seed:
        return []

    parsed = urlparse(seed)
    path = parsed.path.rstrip("/")

    if path.endswith("/chat/completions"):
        return [(seed.rstrip("/"), "chat")]
    if path.endswith("/responses"):
        return [(seed.rstrip("/"), "responses")]

    # If the seed already includes a path (e.g. /v1) treat it as a base path.
    if path:
        base = seed.rstrip("/")
        return [
            (_join_url(base, "chat/completions"), "chat"),
            (_join_url(base, "responses"), "responses"),
        ]

    # Otherwise assume it is only the origin and append the OpenAI-compatible paths.
    with_v1 = _join_url(seed, "v1")
    return [
        (_join_url(with_v1, "chat/completions"), "chat"),
        (_join_url(with_v1, "responses"), "responses"),
    ]


def _candidate_urls():
    """Determine the sequence of URLs to try when contacting the LLM service."""

    env_url = os.environ.get("LLM_API_URL")
    default_seed = "https://litellm-litemaas.apps.prod.rhoai.rh-aiservices-bu.com/v1/chat/completions"
    candidates = OrderedDict()

    for seed in filter(None, [env_url, default_seed]):
        for url, endpoint in _expand_candidate(seed):
            candidates.setdefault((url, endpoint), None)

    # Ensure we also consider the responses endpoint for the default seed.
    for url, endpoint in _expand_candidate(
        "https://litellm-litemaas.apps.prod.rhoai.rh-aiservices-bu.com/v1/responses"
    ):
        candidates.setdefault((url, endpoint), None)

    return list(candidates.keys())


def _extract_message(payload):
    """Extract the textual message from different response schemas."""

    # OpenAI / LiteLLM chat completion format
    choices = payload.get("choices")
    if choices:
        message = choices[0].get("message", {})

        # OpenAI compatible responses normally return a string in "content"
        content = message.get("content", "")
        if isinstance(content, str) and content.strip():
            return content.strip()

        # Some providers (including LiteLLM reasoning models) return a list of
        # message parts. Collect the textual pieces if present.
        if isinstance(content, list):
            parts = []
            for item in content:
                if isinstance(item, str) and item.strip():
                    parts.append(item.strip())
                elif isinstance(item, dict):
                    text = item.get("text") or item.get("value")
                    if isinstance(text, str) and text.strip():
                        parts.append(text.strip())
            if parts:
                return "\n".join(parts)

        # Reasoning models (e.g. DeepSeek-R1) may surface the assistant reply
        # under "reasoning_content" while leaving "content" empty when the
        # response is truncated. Treat it as a fallback so we can surface the
        # provider's output instead of treating it as an empty response.
        reasoning = message.get("reasoning_content")
        if isinstance(reasoning, str) and reasoning.strip():
            return reasoning.strip()

    # OpenAI responses API format
    output = payload.get("output") or payload.get("outputs")
    if output:
        parts = []
        for item in output:
            for content in item.get("content", []):
                if content.get("type") in {"output_text", "text"}:
                    text = content.get("text", "")
                    if text:
                        parts.append(text.strip())
        if parts:
            return "\n".join(part for part in parts if part)

    # Some providers return the message directly at the top level
    for key in ("message", "response", "result"):
        value = payload.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()

    return ""


def maybe_llm_verdict(summary):
    """Optional step that relies on OPENAI_API_KEY to request a qualitative verdict."""

    api_key = os.environ.get("LITELLM_API_KEY") or os.environ.get("OPENAI_API_KEY")
    if not api_key:
        return {
            "llm_used": False,
            "verdict": {
                "status": "PASS" if summary.get("passed") else "FAIL",
                "rationale": _summarize_failures(summary),
            },
            "basis": "deterministic audit rules",
        }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    errors = []

    for api_url, endpoint in _candidate_urls():
        request_body = json.dumps(_llm_payload(summary, endpoint)).encode("utf-8")
        request = urllib.request.Request(
            api_url,
            data=request_body,
            headers=headers,
            method="POST",
        )

        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                raw_body = response.read().decode("utf-8")
                payload = json.loads(raw_body)
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="ignore") if exc.fp else ""
            logging.error("LLM request failed for %s: %s", api_url, body or exc)
            if exc.code in {404, 405}:
                errors.append({"url": api_url, "status": exc.code, "error": body})
                continue
            return {
                "llm_used": False,
                "verdict": f"error contacting LLM (status {exc.code})",
                "error": body or str(exc),
            }
        except (urllib.error.URLError, TimeoutError) as exc:
            logging.error("LLM request error for %s: %s", api_url, exc)
            errors.append({"url": api_url, "error": str(exc)})
            continue
        except json.JSONDecodeError as exc:
            logging.error("Invalid JSON from LLM response: %s", exc)
            return {"llm_used": False, "verdict": "invalid JSON from LLM response"}

        message = _extract_message(payload)

        if not message:
            logging.warning(
                "Empty message from LLM response (%s): %s", api_url, payload
            )
            errors.append({"url": api_url, "error": "empty response", "raw": payload})
            continue

        try:
            verdict = json.loads(message)
        except json.JSONDecodeError:
            verdict = {"status": "UNKNOWN", "rationale": message}

        return {
            "llm_used": True,
            "verdict": verdict,
            "raw": payload,
            "endpoint": api_url,
        }

    return {
        "llm_used": False,
        "verdict": "error contacting LLM",
        "attempts": errors,
    }


def _run_git_command(args: List[str]) -> str:
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as exc:
        logging.warning("git %s failed: %s", " ".join(args), exc)
        return ""


def _determine_base_commit() -> Optional[str]:
    event_path = os.environ.get("GITHUB_EVENT_PATH")
    if event_path and os.path.isfile(event_path):
        try:
            with open(event_path, "r", encoding="utf-8") as fp:
                payload = json.load(fp)
        except (OSError, json.JSONDecodeError) as exc:
            logging.warning("Unable to parse event payload: %s", exc)
        else:
            pr = payload.get("pull_request")
            if isinstance(pr, dict):
                sha = pr.get("base", {}).get("sha")
                if sha:
                    return sha
            before = payload.get("before")
            if isinstance(before, str) and before.strip():
                return before.strip()

    base_ref = os.environ.get("GITHUB_BASE_REF")
    if base_ref:
        ref = f"origin/{base_ref}"
        sha = _run_git_command(["rev-parse", ref])
        if sha:
            return sha

    sha = _run_git_command(["rev-parse", "HEAD^"])
    return sha or None


def collect_change_summary() -> Dict[str, object]:
    base = _determine_base_commit()
    summary: Dict[str, object] = {}
    if base:
        summary["base_commit"] = base
        names = _run_git_command(["diff", f"{base}...HEAD", "--name-only"])
        if names:
            files = [line for line in names.splitlines() if line.strip()]
            summary["changed_files"] = files
            summary["changed_file_count"] = len(files)
        diffstat = _run_git_command(["diff", f"{base}...HEAD", "--stat"])
        if diffstat:
            lines = diffstat.splitlines()
            if len(lines) > 20:
                lines = lines[:19] + ["…" + lines[-1]]
            summary["diffstat"] = "\n".join(lines)
    else:
        logging.info("Unable to determine base commit; diff summary unavailable")

    return summary


def _github_request(
    method: str,
    path: str,
    token: str,
    payload: Optional[Dict[str, object]] = None,
) -> Dict[str, object]:
    url = f"{GITHUB_API_URL.rstrip('/')}/{path.lstrip('/')}"
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
    }
    if data is not None:
        headers["Content-Type"] = "application/json"

    request = urllib.request.Request(url, data=data, headers=headers, method=method)
    with urllib.request.urlopen(request, timeout=30) as response:
        body = response.read().decode("utf-8")
    return json.loads(body) if body else {}


def _ensure_label(
    repo: str, token: str, name: str, color: str, description: str
) -> None:
    try:
        _github_request("GET", f"/repos/{repo}/labels/{quote(name)}", token)
        return
    except urllib.error.HTTPError as exc:
        if exc.code != 404:
            raise

    payload = {"name": name, "color": color, "description": description}
    try:
        _github_request("POST", f"/repos/{repo}/labels", token, payload)
    except urllib.error.HTTPError as exc:
        # Ignore race conditions where another workflow created it first
        if exc.code != 422:
            raise


def _find_existing_issue(
    repo: str, token: str, fingerprint: str
) -> Optional[Dict[str, object]]:
    params = f"state=open&labels={quote('automation:audit')}"  # urlencoded
    try:
        issues = _github_request(
            "GET", f"/repos/{repo}/issues?{params}&per_page=100", token
        )
    except urllib.error.HTTPError as exc:
        logging.warning("Unable to list issues: %s", exc)
        return None

    if isinstance(issues, list):
        marker = f"<!-- audit-fingerprint: {fingerprint} -->"
        for issue in issues:
            if marker in issue.get("body", ""):
                return issue
    return None


def maybe_create_issue(summary: Dict[str, object]) -> Dict[str, object]:
    failing_rules = [
        item.get("rule", "unknown")
        for item in summary.get("breakdown", [])
        if not item.get("ok", False)
    ]

    if not failing_rules:
        return {"created": False, "reason": "no failing rules"}

    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    repo = os.environ.get("GITHUB_REPOSITORY")
    if not token or not repo:
        return {"created": False, "reason": "missing GitHub credentials"}

    fingerprint = "|".join(sorted(failing_rules))
    try:
        _ensure_label(
            repo,
            token,
            "automation:audit",
            color="0E8A16",
            description="Automated audit improvements",
        )
    except Exception as exc:  # pragma: no cover
        logging.error("Unable to ensure audit label: %s", exc)
        return {"created": False, "error": str(exc)}

    existing = _find_existing_issue(repo, token, fingerprint)
    if existing:
        logging.info(
            "Audit improvement already tracked in issue #%s", existing.get("number")
        )
        return {
            "created": False,
            "reason": "existing issue",
            "issue": {
                "number": existing.get("number"),
                "url": existing.get("html_url"),
            },
        }

    diff = summary.get("changes", {})
    body_lines = [
        "## Audit improvement opportunity",
        "",
        "The automated audit detected the following failing rules:",
    ]
    for rule in failing_rules:
        body_lines.append(f"- `{rule}`")

    body_lines.extend(
        [
            "",
            "### Suggested next steps",
            "- Review the failing rule(s) and propose concrete improvements.",
            "- Use the local LLM workflow to draft changes that address the issues.",
            "- Open a pull request referencing this issue and ensure the audit passes.",
        ]
    )

    if diff:
        body_lines.extend(["", "### Context from the triggering run"])
        base_commit = diff.get("base_commit")
        if base_commit:
            body_lines.append(f"- Base commit: `{base_commit}`")
        file_count = diff.get("changed_file_count")
        if file_count:
            body_lines.append(f"- Files changed: {file_count}")
        changed_files = diff.get("changed_files", [])
        if changed_files:
            preview = "\n".join(f"  - {name}" for name in changed_files[:15])
            if preview:
                body_lines.extend(["- Sample of changed files:", preview])
        diffstat = diff.get("diffstat")
        if diffstat:
            body_lines.extend(["", "```", diffstat, "```"])

    body_lines.extend(
        [
            "",
            f"<!-- audit-fingerprint: {fingerprint} -->",
        ]
    )

    payload = {
        "title": f"Audit improvement: {', '.join(failing_rules[:3])}",
        "body": "\n".join(body_lines),
        "labels": ["automation:audit"],
    }

    try:
        response = _github_request("POST", f"/repos/{repo}/issues", token, payload)
    except urllib.error.HTTPError as exc:
        error_body = exc.read().decode("utf-8", errors="ignore") if exc.fp else str(exc)
        logging.error("Unable to create audit issue: %s", error_body)
        return {"created": False, "error": error_body or str(exc)}

    logging.info("Created audit improvement issue #%s", response.get("number"))
    return {
        "created": True,
        "issue": {
            "number": response.get("number"),
            "url": response.get("html_url"),
        },
    }


def main():
    rubric = load_yaml(os.path.join(AUDIT, "rubric.yml"))
    score, breakdown = score_rules(rubric.get("rules", {}))
    thresholds = rubric.get("thresholds", {})
    pass_score = thresholds.get("pass_score", 30)
    inputs = summarize_audit_inputs()
    changes = collect_change_summary()

    summary = {
        "score": score,
        "pass_score": pass_score,
        "passed": score >= pass_score,
        "breakdown": breakdown,
        "audit_inputs": inputs,
    }
    if changes:
        summary["changes"] = changes
    summary["failing_rules"] = [
        item.get("rule", "unknown") for item in breakdown if not item.get("ok", False)
    ]
    print(json.dumps(summary, ensure_ascii=False, indent=2))

    llm = maybe_llm_verdict(summary)
    print(json.dumps({"llm_evaluation": llm}, ensure_ascii=False))

    issue = maybe_create_issue(summary)
    print(json.dumps({"improvement_issue": issue}, ensure_ascii=False))

    if score < pass_score:
        print("Audit NOK: score below threshold.")
        sys.exit(2)

    print("Audit OK.")
    sys.exit(0)


if __name__ == "__main__":
    main()
