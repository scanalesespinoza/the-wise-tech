#!/usr/bin/env python3
import os
import sys
import yaml
import json

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
AUDIT = os.path.join(ROOT, "audit")


def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def file_contains(path, substrings):
    try:
        with open(os.path.join(ROOT, path), "r", encoding="utf-8", errors="ignore") as f:
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
            count = sum(1 for f in os.listdir(directory) if f.endswith((".yml", ".yaml")))
            if sub == "personas":
                personas = count
            if sub == "escenarios":
                scenarios = count
            if sub == "impactos":
                impacts = count
    return {"personas": personas, "scenarios": scenarios, "impacts": impacts}


def maybe_llm_verdict(summary_text):
    """Optional step that relies on OPENAI_API_KEY to request a qualitative verdict."""

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        return {"llm_used": False, "verdict": "skipped (no OPENAI_API_KEY)"}

    # To keep CI secure by default, the actual API request is left unimplemented.
    # Integrate your LLM client here if you want to enable this step.
    return {"llm_used": False, "verdict": "disabled in this repo by default"}


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

    llm = maybe_llm_verdict(json.dumps(summary, ensure_ascii=False))
    print(json.dumps({"llm_evaluation": llm}, ensure_ascii=False))

    if score < pass_score:
        print("Audit NOK: score below threshold.")
        sys.exit(2)

    print("Audit OK.")
    sys.exit(0)


if __name__ == "__main__":
    main()
