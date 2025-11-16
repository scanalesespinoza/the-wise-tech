#!/usr/bin/env python3
import json
import sys

import yaml

OK = "\033[92mOK\033[0m"
ERR = "\033[91mERR\033[0m"


def in_range(val, low, high, inclusive=True):
    if inclusive:
        return low <= val <= high
    return low < val < high


def expect_bool(d, k, errs):
    if k not in d or not isinstance(d[k], bool):
        errs.append(f"{k} must be boolean")
    return d.get(k)


def expect_int(d, k, errs, low=None, high=None):
    if k not in d or not isinstance(d[k], int):
        errs.append(f"{k} must be an integer")
        return None
    v = d[k]
    if low is not None and high is not None and not in_range(v, low, high):
        errs.append(f"{k} out of range [{low},{high}]: {v}")
    return v


def expect_float(d, k, errs, low=None, high=None):
    if k not in d or not isinstance(d[k], (int, float)):
        errs.append(f"{k} must be numeric")
        return None
    v = float(d[k])
    if low is not None and high is not None and not in_range(v, low, high):
        errs.append(f"{k} out of range [{low},{high}]: {v}")
    return v


def main(path):
    with open(path, "r", encoding="utf-8") as f:
        doc = yaml.safe_load(f)

    errs = []
    # required base fields
    for k in [
        "service",
        "version",
        "timeouts_ms",
        "retries",
        "circuit_breaker",
        "bulkhead",
        "cache",
    ]:
        if k not in doc:
            errs.append(f"Missing required key: {k}")

    # timeouts
    t = doc.get("timeouts_ms", {})
    for k in t:
        if not isinstance(t[k], int) or t[k] <= 0 or t[k] > 120000:
            errs.append(f"timeouts_ms.{k} must be an integer within 1..120000 ms")

    # retries
    r = doc.get("retries", {})
    if isinstance(r, dict):
        enabled = expect_bool(r, "enabled", errs)
        if enabled:
            expect_int(r, "max_attempts", errs, 1, 10)
            backoff = r.get("backoff")
            if backoff not in ("fixed", "linear", "exponential"):
                errs.append("retries.backoff must be fixed|linear|exponential")
            expect_int(r, "base_ms", errs, 10, 60000)

    # circuit breaker
    cb = doc.get("circuit_breaker", {})
    if isinstance(cb, dict):
        cb_enabled = expect_bool(cb, "enabled", errs)
        if cb_enabled:
            expect_float(cb, "failure_threshold", errs, 0.0, 1.0)
            expect_int(cb, "min_samples", errs, 1, 100000)
            expect_int(cb, "reset_timeout_ms", errs, 100, 600000)

    # bulkhead
    bh = doc.get("bulkhead", {})
    if isinstance(bh, dict):
        bh_enabled = expect_bool(bh, "enabled", errs)
        if bh_enabled:
            expect_int(bh, "max_concurrent", errs, 1, 100000)

    # cache
    c = doc.get("cache", {})
    if isinstance(c, dict):
        c_enabled = expect_bool(c, "enabled", errs)
        if c_enabled:
            expect_int(c, "ttl_s", errs, 1, 86400)

    if errs:
        print(f"{ERR} Resilience validation failed for {path}:")
        for e in errs:
            print(f" - {e}")
        sys.exit(1)
    else:
        print(f"{OK} {path} is valid.")
        # optional JSON output for CI debugging
        print(
            json.dumps(
                {"service": doc.get("service"), "version": doc.get("version")},
                ensure_ascii=False,
            )
        )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(
            "Usage: python operations/scripts/validate-resilience.py experience/scenarios/payments/policies/resilience.yml"
        )
        sys.exit(2)
    main(sys.argv[1])
