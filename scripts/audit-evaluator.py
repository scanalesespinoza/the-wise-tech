#!/usr/bin/env python3
import os
import sys
import yaml
import json
import logging
import urllib.error
import urllib.request

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
AUDIT = os.path.join(ROOT, "audit")


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


def _llm_payload(summary):
    model = os.environ.get("LLM_MODEL", "gpt-4o-mini")
    system_prompt = (
        "You are assisting with an internal audit. Given the JSON summary of the "
        "automated checks, return a short JSON object with the fields 'status' "
        "(values: PASS or FAIL) and 'rationale' (a concise explanation)."
    )
    summary_text = json.dumps(summary, ensure_ascii=False)
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


def maybe_llm_verdict(summary):
    """Optional step that relies on OPENAI_API_KEY to request a qualitative verdict."""

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        return {
            "llm_used": False,
            "verdict": {
                "status": "PASS" if summary.get("passed") else "FAIL",
                "rationale": _summarize_failures(summary),
            },
            "basis": "deterministic audit rules",
        }

    api_url = os.environ.get(
        "LLM_API_URL", "https://api.openai.com/v1/chat/completions"
    )

    request_body = json.dumps(_llm_payload(summary)).encode("utf-8")
    request = urllib.request.Request(
        api_url,
        data=request_body,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            raw_body = response.read().decode("utf-8")
            payload = json.loads(raw_body)
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="ignore") if exc.fp else ""
        logging.error("LLM request failed: %s", body or exc)
        return {
            "llm_used": False,
            "verdict": f"error contacting LLM (status {exc.code})",
            "error": body or str(exc),
        }
    except (urllib.error.URLError, TimeoutError) as exc:
        logging.error("LLM request error: %s", exc)
        return {"llm_used": False, "verdict": f"error contacting LLM: {exc}"}
    except json.JSONDecodeError as exc:
        logging.error("Invalid JSON from LLM response: %s", exc)
        return {"llm_used": False, "verdict": "invalid JSON from LLM response"}

    message = (
        payload.get("choices", [{}])[0].get("message", {}).get("content", "").strip()
    )

    if not message:
        logging.warning("Empty message from LLM response: %s", payload)
        return {"llm_used": False, "verdict": "empty LLM response", "raw": payload}

    try:
        verdict = json.loads(message)
    except json.JSONDecodeError:
        verdict = {"status": "UNKNOWN", "rationale": message}

    return {
        "llm_used": True,
        "verdict": verdict,
        "raw": payload,
    }


def main():
    rubric = load_yaml(os.path.join(AUDIT, "rubric.yml"))
    score, breakdown = score_rules(rubric.get("rules", {}))
    thresholds = rubric.get("thresholds", {})
    pass_score = thresholds.get("pass_score", 30)
    inputs = summarize_audit_inputs()

    summary = {
        "score": score,
        "pass_score": pass_score,
        "passed": score >= pass_score,
        "breakdown": breakdown,
        "audit_inputs": inputs,
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))

    llm = maybe_llm_verdict(summary)
    print(json.dumps({"llm_evaluation": llm}, ensure_ascii=False))

    if score < pass_score:
        print("Audit NOK: score below threshold.")
        sys.exit(2)

    print("Audit OK.")
    sys.exit(0)


if __name__ == "__main__":
    main()
