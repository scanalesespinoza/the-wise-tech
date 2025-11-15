#!/usr/bin/env python3
import sys

import yaml

OK = "\033[92mOK\033[0m"
ERR = "\033[91mERR\033[0m"


def num(v):
    return isinstance(v, (int, float))


def pct(v):
    return num(v) and 0.0 <= float(v) <= 100.0


def pos(v):
    return num(v) and float(v) > 0.0


def main(path):
    with open(path, "r", encoding="utf-8") as f:
        doc = yaml.safe_load(f)

    errs = []
    for k in ["service", "version", "objectives", "error_budget_policies"]:
        if k not in doc:
            errs.append(f"Falta clave requerida: {k}")

    obj = doc.get("objectives", {})
    if not isinstance(obj, dict) or not obj:
        errs.append("objectives debe ser un mapa con al menos 1 objetivo")

    # availability
    if "availability" in obj:
        a = obj["availability"]
        if not pct(a.get("target", -1)):
            errs.append("availability.target debe ser 0..100 (%)")
        if not a.get("window"):
            errs.append("availability.window requerido (p.ej., 30d)")

    # latency_p95_ms
    if "latency_p95_ms" in obj:
        latency = obj["latency_p95_ms"]
        if not pos(latency.get("target", -1)):
            errs.append("latency_p95_ms.target debe ser > 0 (ms)")
        if not latency.get("window"):
            errs.append("latency_p95_ms.window requerido (p.ej., 30d)")

    # error budget policies
    eb = doc.get("error_budget_policies", [])
    if not isinstance(eb, list) or not eb:
        errs.append("error_budget_policies debe ser una lista no vacía")

    if errs:
        print(f"{ERR} Validación SLO falló en {path}:")
        for e in errs:
            print(" -", e)
        sys.exit(1)
    print(f"{OK} {path} válido.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(
            "Uso: python operations/scripts/validate-slos.py experience/scenarios/payments/slo/slo-spec.yml"
        )
        sys.exit(2)
    main(sys.argv[1])
