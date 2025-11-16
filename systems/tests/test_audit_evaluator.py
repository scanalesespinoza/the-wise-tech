import importlib.util
import os
import pathlib
import sys
import tempfile
import textwrap
import unittest
from unittest import mock

MODULE_PATH = (
    pathlib.Path(__file__).resolve().parents[2]
    / "operations"
    / "scripts"
    / "audit-evaluator.py"
)
SPEC = importlib.util.spec_from_file_location("audit_evaluator", MODULE_PATH)
audit_evaluator = importlib.util.module_from_spec(SPEC)
sys.modules.setdefault("audit_evaluator", audit_evaluator)
SPEC.loader.exec_module(audit_evaluator)


class CandidateUrlTests(unittest.TestCase):
    def setUp(self):
        self.original_llm_url = os.environ.get("LLM_API_URL")
        os.environ.pop("LLM_API_URL", None)
        self.addCleanup(self._restore_env)

    def _restore_env(self):
        if self.original_llm_url is None:
            os.environ.pop("LLM_API_URL", None)
        else:
            os.environ["LLM_API_URL"] = self.original_llm_url

    def test_default_candidates_include_chat_and_responses(self):
        candidates = audit_evaluator._candidate_urls()
        urls = [item[0] for item in candidates]
        self.assertTrue(urls[0].endswith("/v1/chat/completions"))
        self.assertTrue(any(url.endswith("/v1/responses") for url in urls))

    def test_base_url_without_path_appends_v1(self):
        with mock.patch.dict(
            os.environ, {"LLM_API_URL": "https://example.com"}, clear=False
        ):
            candidates = audit_evaluator._candidate_urls()
        urls = [item[0] for item in candidates]
        self.assertIn("https://example.com/v1/chat/completions", urls)
        self.assertIn("https://example.com/v1/responses", urls)

    def test_base_url_with_path_reuses_path(self):
        with mock.patch.dict(
            os.environ, {"LLM_API_URL": "https://example.com/api"}, clear=False
        ):
            candidates = audit_evaluator._candidate_urls()
        urls = [item[0] for item in candidates]
        self.assertIn("https://example.com/api/chat/completions", urls)
        self.assertIn("https://example.com/api/responses", urls)


class ExtractMessageTests(unittest.TestCase):
    def test_extracts_from_chat_completion(self):
        payload = {"choices": [{"message": {"content": '{"status": "PASS"}'}}]}
        message = audit_evaluator._extract_message(payload)
        self.assertEqual('{"status": "PASS"}', message)

    def test_extracts_from_responses_format(self):
        payload = {
            "output": [
                {"content": [{"type": "output_text", "text": '{"status": "FAIL"}'}]}
            ]
        }
        message = audit_evaluator._extract_message(payload)
        self.assertEqual('{"status": "FAIL"}', message)

    def test_extracts_from_top_level_string(self):
        payload = {"response": '{"status": "UNKNOWN"}'}
        message = audit_evaluator._extract_message(payload)
        self.assertEqual('{"status": "UNKNOWN"}', message)


class RoadmapContextTests(unittest.TestCase):
    def test_extracts_context_from_sample_file(self):
        sample = textwrap.dedent(
            """
            # Implementation Roadmap

            ## Current state (Release 01)
            - Repository mapped.

            ## Stages to reach a consumable product
            ### Stage 1 — Discovery ✅
            Objective: Document the current assets.

            ### Stage 2 — Navigable MVP
            Objective: Package a guided flow.

            ## Immediate next steps
            1. Prepare flow
            2. Automate checks
            """
        )
        with tempfile.NamedTemporaryFile("w", delete=False, encoding="utf-8") as handle:
            handle.write(sample)
            path = handle.name
        try:
            context = audit_evaluator.extract_roadmap_context(path)
        finally:
            os.unlink(path)

        self.assertEqual(
            context.get("current_state_heading"), "Current state (Release 01)"
        )
        self.assertIn("Prepare flow", context.get("immediate_next_steps", []))
        next_stage = context.get("next_stage") or {}
        self.assertEqual(next_stage.get("title"), "Stage 2 — Navigable MVP")
        self.assertTrue(next_stage.get("summary"))

    def test_missing_file_returns_empty_context(self):
        missing = os.path.join(tempfile.gettempdir(), "roadmap-not-found.md")
        if os.path.exists(missing):
            os.unlink(missing)
        self.assertEqual({}, audit_evaluator.extract_roadmap_context(missing))


if __name__ == "__main__":
    unittest.main()
