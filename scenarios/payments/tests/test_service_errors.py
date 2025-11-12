import unittest

from scenarios.payments.service.errors import (
    PaymentDeclined,
    PaymentTimeout,
    PaymentUnknownFailure,
    RemediationHint,
    map_exception_to_http,
)


class PaymentErrorMappingTests(unittest.TestCase):
    def setUp(self) -> None:
        self.hint = RemediationHint(
            action_en="Escalate to payments squad",
            action_es="Escalar al escuadrón de pagos",
            runbook="scenarios/payments/docs/en/runbook.md",
        )

    def test_declined_payment_maps_to_402(self) -> None:
        error = PaymentDeclined(reason="DECLINED", hint=self.hint)
        status, code = map_exception_to_http(error)
        self.assertEqual(status, 402)
        self.assertEqual(code, "PAYMENT_DECLINED")
        self.assertIn("PAYMENT_DECLINED", error.translate("en"))
        self.assertIn("PAYMENT_DECLINED", error.translate("es"))

    def test_timeout_maps_to_gateway_timeout(self) -> None:
        error = PaymentTimeout(provider="stripe", hint=self.hint)
        status, code = map_exception_to_http(error)
        self.assertEqual(status, 504)
        self.assertEqual(code, "PAYMENT_TIMEOUT")

    def test_unknown_failure_maps_to_bad_gateway(self) -> None:
        error = PaymentUnknownFailure(
            provider="adyen",
            reference_id="ref-123",
            hint=self.hint,
        )
        status, code = map_exception_to_http(error)
        self.assertEqual(status, 502)
        self.assertEqual(code, "PAYMENT_UNKNOWN")
        self.assertIn("ref-123", error.reference_id)


if __name__ == "__main__":
    unittest.main()
