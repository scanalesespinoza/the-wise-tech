"""Sliding-window rate limiter demo."""

from __future__ import annotations

import collections
import random
import time
from dataclasses import dataclass


@dataclass
class RequestResult:
    allowed: bool
    reason: str
    tokens_remaining: float


class SlidingWindowLimiter:
    def __init__(self, max_tokens: int, refill_per_second: float) -> None:
        self.max_tokens = float(max_tokens)
        self.tokens = float(max_tokens)
        self.refill_per_second = refill_per_second
        self.last_refill = time.monotonic()

    def _refill(self) -> None:
        now = time.monotonic()
        elapsed = now - self.last_refill
        self.tokens = min(
            self.max_tokens, self.tokens + elapsed * self.refill_per_second
        )
        self.last_refill = now

    def allow(self, tokens: float = 1.0) -> RequestResult:
        self._refill()
        if tokens <= self.tokens:
            self.tokens -= tokens
            return RequestResult(True, "accepted", self.tokens)
        return RequestResult(False, "shed", self.tokens)


def generate_requests(count: int = 30):
    """Return a deque of synthetic request costs."""
    return collections.deque(random.uniform(0.5, 1.5) for _ in range(count))


def run_simulation() -> None:
    limiter = SlidingWindowLimiter(max_tokens=10, refill_per_second=2)
    requests = generate_requests()
    while requests:
        cost = requests.popleft()
        result = limiter.allow(cost)
        status = "✅" if result.allowed else "⚠️"
        print(
            f"{status} cost={cost:.2f} tokens_remaining={result.tokens_remaining:.2f} ({result.reason})"
        )
        time.sleep(0.2)


if __name__ == "__main__":
    run_simulation()
