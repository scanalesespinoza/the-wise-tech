"""Structured logging and trace propagation example."""

from __future__ import annotations

import json
import time
import uuid
from contextlib import contextmanager
from dataclasses import dataclass
from typing import Iterator


@dataclass
class TraceContext:
    trace_id: str
    span_id: str


@contextmanager
def span(name: str, parent: TraceContext | None = None) -> Iterator[TraceContext]:
    context = TraceContext(
        trace_id=parent.trace_id if parent else uuid.uuid4().hex,
        span_id=uuid.uuid4().hex[:16],
    )
    log_event(
        "span.start",
        name=name,
        context=context,
        parent_span_id=getattr(parent, "span_id", None),
    )
    start = time.time()
    try:
        yield context
    finally:
        duration_ms = (time.time() - start) * 1000
        log_event(
            "span.end",
            name=name,
            context=context,
            duration_ms=round(duration_ms, 2),
            parent_span_id=getattr(parent, "span_id", None),
        )


def log_event(event: str, *, name: str, context: TraceContext, **extra: object) -> None:
    payload = {
        "event": event,
        "name": name,
        "trace_id": context.trace_id,
        "span_id": context.span_id,
        **extra,
    }
    print(json.dumps(payload))


def write_entity(entity_id: str) -> None:
    with span("write_entity") as root:
        log_event(
            "entity.validation", name="validate", context=root, entity_id=entity_id
        )
        time.sleep(0.05)
        with span("persist", parent=root) as persist_span:
            log_event(
                "entity.persist",
                name="persist",
                context=persist_span,
                entity_id=entity_id,
            )
            time.sleep(0.02)
        with span("emit_metric", parent=root):
            log_event(
                "metric",
                name="write.success",
                context=root,
                entity_id=entity_id,
                value=1,
            )


if __name__ == "__main__":
    write_entity("user-123")
