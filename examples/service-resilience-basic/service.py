"""Minimal simulation of a resilient dependency call."""

from __future__ import annotations

import random
import time
from dataclasses import dataclass


@dataclass
class DependencyResponse:
    status: str
    latency_ms: int
    attempt: int
    fallback_used: bool


def call_dependency(max_latency_ms: int = 900, failure_rate: float = 0.35) -> int:
    """Return latency for a dependency call or raise on timeout/failure."""
    latency = random.randint(100, max_latency_ms)
    if latency > 800:
        raise TimeoutError(f"dependency timed out at {latency} ms")
    if random.random() < failure_rate:
        raise ConnectionError("dependency returned HTTP 500")
    time.sleep(latency / 1000.0)
    return latency


def invoke_with_resilience(max_attempts: int = 3) -> DependencyResponse:
    for attempt in range(1, max_attempts + 1):
        try:
            latency = call_dependency()
            return DependencyResponse("success", latency, attempt, False)
        except (TimeoutError, ConnectionError) as exc:
            print(f"attempt {attempt} failed: {exc}")
            time.sleep(0.05 * attempt)  # jittered backoff
    print("falling back to async confirmation queue…")
    return DependencyResponse(
        "degraded", latency_ms=0, attempt=max_attempts, fallback_used=True
    )


if __name__ == "__main__":
    response = invoke_with_resilience()
    print(response)
