#!/usr/bin/env python3
"""
Simplified mock calculation of error budget consumption.
Input: SLO YAML + optional local metrics (JSON/YAML) or simulated rates.
Output: % of budget spent and any triggered policies.
"""

import json
import sys

import yaml


def load(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main(spec_path, metrics_path=None):
    spec = load(spec_path)
    # MOCK: if there are no metrics, fall back to simulated values
    metrics = {"availability": 99.0, "latency_p95_ms": 420}
    if metrics_path:
        with open(metrics_path, "r", encoding="utf-8") as f:
            metrics.update(json.load(f))

    targets = spec["objectives"]
    # Extremely simplified calculation: percentage of over-consumption per objective
    spent = 0.0
    if "availability" in targets:
        target = float(targets["availability"]["target"])
        current = float(metrics.get("availability", target))
        # budget spent ~ relative loss of availability
        if current < target:
            spent += min(100.0, (target - current) * 2)  # basic heuristic

    if "latency_p95_ms" in targets:
        target = float(targets["latency_p95_ms"]["target"])
        current = float(metrics.get("latency_p95_ms", target))
        if current > target:
            over = ((current - target) / target) * 100.0
            spent += min(100.0, over * 0.5)  # basic heuristic

    spent = max(0.0, min(spent, 100.0))
    print(json.dumps({"error_budget_spent": round(spent, 2)}, ensure_ascii=False))

    # List triggered policies
    policies = []
    for p in spec.get("error_budget_policies", []):
        cond = p.get("condition", "").replace("error_budget_spent", str(spent))
        try:
            if eval(cond):
                policies.append({"name": p["name"], "actions": p.get("actions", [])})
        except Exception:
            pass

    print(json.dumps({"policies_triggered": policies}, ensure_ascii=False))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(
            "Usage: python operations/scripts/check-error-budget.py experience/scenarios/payments/slo/slo-spec.yml [metrics.json]"
        )
        sys.exit(2)
    spec = sys.argv[1]
    metrics = sys.argv[2] if len(sys.argv) > 2 else None
    main(spec, metrics)
