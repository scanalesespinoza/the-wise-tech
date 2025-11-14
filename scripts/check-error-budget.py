#!/usr/bin/env python3
"""
Cálculo simplificado de consumo de presupuesto de error (mock).
Entrada: YAML SLO + métricas locales (JSON/YAML opcional) o tasas simuladas.
Salida: % de budget gastado y políticas aplicables.
"""

import json
import sys

import yaml


def load(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main(spec_path, metrics_path=None):
    spec = load(spec_path)
    # MOCK: si no hay métricas, usar valores simulados
    metrics = {"availability": 99.0, "latency_p95_ms": 420}
    if metrics_path:
        with open(metrics_path, "r", encoding="utf-8") as f:
            metrics.update(json.load(f))

    targets = spec["objectives"]
    # Cálculo MUY simplificado: porcentaje de sobre-consumo en cada objetivo
    spent = 0.0
    if "availability" in targets:
        target = float(targets["availability"]["target"])
        current = float(metrics.get("availability", target))
        # budget gastado ~ pérdida relativa de disponibilidad
        if current < target:
            spent += min(100.0, (target - current) * 2)  # heurística simple

    if "latency_p95_ms" in targets:
        target = float(targets["latency_p95_ms"]["target"])
        current = float(metrics.get("latency_p95_ms", target))
        if current > target:
            over = ((current - target) / target) * 100.0
            spent += min(100.0, over * 0.5)  # heurística simple

    spent = max(0.0, min(spent, 100.0))
    print(json.dumps({"error_budget_spent": round(spent, 2)}, ensure_ascii=False))

    # Listar políticas aplicables
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
            "Uso: python scripts/check-error-budget.py platform/slo/slo-spec.yml [metrics.json]"
        )
        sys.exit(2)
    spec = sys.argv[1]
    metrics = sys.argv[2] if len(sys.argv) > 2 else None
    main(spec, metrics)
