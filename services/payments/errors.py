"""Domain-specific exceptions for the payments service.

The module is bilingual by design: docstrings include English and Spanish
context so teams across regions can share the same artifacts.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


class PaymentsError(Exception):
    """Base error for payment operations / Error base para operaciones de pago."""

    def __init__(self, message_en: str, message_es: str, *, code: str) -> None:
        super().__init__(message_en)
        self.message_en = message_en
        self.message_es = message_es
        self.code = code

    def __str__(self) -> str:
        return f"[{self.code}] {self.message_en}"

    def translate(self, language: str) -> str:
        """Return the human message in the requested language."""
        if language.lower().startswith("es"):
            return f"[{self.code}] {self.message_es}"
        return f"[{self.code}] {self.message_en}"


@dataclass(frozen=True)
class RemediationHint:
    """Guides support agents on next steps / Guía para agentes de soporte."""

    action_en: str
    action_es: str
    runbook: Optional[str] = None


class PaymentDeclined(PaymentsError):
    """Card was declined by issuer / La tarjeta fue rechazada por el emisor."""

    def __init__(self, *, reason: str, hint: RemediationHint) -> None:
        super().__init__(
            "Payment declined by issuer. Ask the customer to contact their bank.",
            "El pago fue rechazado por el banco emisor. Solicita a la persona cliente que contacte a su banco.",
            code="PAYMENT_DECLINED",
        )
        self.reason = reason
        self.hint = hint


class PaymentTimeout(PaymentsError):
    """Downstream provider timed out / El proveedor aguas abajo excedió el tiempo."""

    def __init__(self, *, provider: str, hint: RemediationHint) -> None:
        super().__init__(
            "Payment provider timeout. Retry with exponential backoff or trigger manual review.",
            "Tiempo de espera agotado en el proveedor de pagos. Reintenta con backoff exponencial o activa revisión manual.",
            code="PAYMENT_TIMEOUT",
        )
        self.provider = provider
        self.hint = hint


class PaymentUnknownFailure(PaymentsError):
    """Unexpected provider response / Respuesta inesperada del proveedor."""

    def __init__(self, *, provider: str, reference_id: str, hint: RemediationHint) -> None:
        super().__init__(
            "Unknown failure from provider. Escalate with context attached.",
            "Fallo desconocido del proveedor. Escala el incidente con contexto adjunto.",
            code="PAYMENT_UNKNOWN",
        )
        self.provider = provider
        self.reference_id = reference_id
        self.hint = hint


def map_exception_to_http(error: PaymentsError) -> tuple[int, str]:
    """Convert domain errors into HTTP status + machine-readable code."""

    if isinstance(error, PaymentDeclined):
        return 402, error.code
    if isinstance(error, PaymentTimeout):
        return 504, error.code
    if isinstance(error, PaymentUnknownFailure):
        return 502, error.code
    return 500, "PAYMENT_ERROR"
