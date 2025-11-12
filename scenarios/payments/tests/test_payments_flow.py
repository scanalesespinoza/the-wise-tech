"""Validate payments fixtures and bilingual metadata."""

from __future__ import annotations

import json
from pathlib import Path
import unittest

FIXTURES_DIR = Path(__file__).parent / "fixtures"


class PaymentsFlowFixtureTests(unittest.TestCase):
    def load_fixture(self, filename: str) -> dict:
        fixture_path = FIXTURES_DIR / filename
        self.assertTrue(fixture_path.exists(), f"Missing fixture: {filename}")
        return json.loads(fixture_path.read_text(encoding="utf-8"))

    def test_valid_charge_fixture_contains_translations(self) -> None:
        data = self.load_fixture("valid-charge.json")
        self.assertEqual(data["status_en"], "approved")
        self.assertEqual(data["status_es"], "aprobado")
        self.assertTrue(data.get("correlation_id"))
        self.assertIn("notes_en", data["metadata"])
        self.assertIn("notes_es", data["metadata"])

    def test_refund_fixture_is_idempotent_friendly(self) -> None:
        data = self.load_fixture("refund-request.json")
        self.assertTrue(data["idempotency_key"].startswith("refund-"))
        self.assertEqual(data["charge_id"], "ch_12345")
        self.assertEqual(data["amount"], 1250)
        self.assertEqual(data["reason_en"], "customer-request")
        self.assertEqual(data["reason_es"], "solicitud-cliente")


if __name__ == "__main__":
    unittest.main()
