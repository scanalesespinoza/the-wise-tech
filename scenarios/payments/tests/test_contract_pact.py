import json
import unittest
from pathlib import Path


PACT_FILE = Path("scenarios/payments/contracts/payments/v2/pacts/checkout-ui-payments.json")


class PactContractTests(unittest.TestCase):
    def test_pact_file_exists(self) -> None:
        self.assertTrue(PACT_FILE.exists(), "Pact file should exist for the scenario")

    def test_consumer_and_provider_are_named(self) -> None:
        data = json.loads(PACT_FILE.read_text())
        self.assertEqual(data["consumer"]["name"], "checkout-ui")
        self.assertEqual(data["provider"]["name"], "payments")

    def test_interactions_are_documented(self) -> None:
        data = json.loads(PACT_FILE.read_text())
        self.assertGreaterEqual(len(data.get("interactions", [])), 1)
        interaction = data["interactions"][0]
        self.assertEqual(interaction["request"]["method"], "POST")
        self.assertEqual(interaction["response"]["status"], 201)
        self.assertIn("language", data.get("metadata", {}))
        self.assertIn("en", data["metadata"]["language"])
        self.assertIn("es", data["metadata"]["language"])


if __name__ == "__main__":
    unittest.main()
