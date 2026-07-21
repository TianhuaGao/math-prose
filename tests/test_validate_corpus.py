from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_corpus", ROOT / "scripts" / "validate_corpus.py"
)
assert SPEC and SPEC.loader
validate_corpus = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validate_corpus)


class CorpusValidationTests(unittest.TestCase):
    def test_math_core_passes_readiness_gate(self) -> None:
        records, parse_errors = validate_corpus.read_jsonl(
            [str(ROOT / "references" / "corpora" / "math-core.jsonl")]
        )
        self.assertEqual(validate_corpus.validate(records, parse_errors), [])
        self.assertEqual(validate_corpus.validate_core_readiness(records), [])

    def test_small_core_fails_readiness_gate(self) -> None:
        records, _ = validate_corpus.read_jsonl(
            [str(ROOT / "references" / "corpora" / "math-core.jsonl")]
        )
        errors = validate_corpus.validate_core_readiness(records[:1])
        self.assertTrue(any("anchor sources" in error for error in errors))
        self.assertTrue(any("observations" in error for error in errors))
        self.assertTrue(any("anchor disciplines" in error for error in errors))

    def test_pattern_sources_require_matching_behavior_observations(self) -> None:
        source = {
            "_location": "test:1",
            "id": "src-test",
            "record_type": "source",
            "corpus_layer": "core",
            "source_role": "anchor",
            "title": "Test",
            "year": 2026,
            "discipline": "pure-mathematics",
            "citation": "Test citation",
            "access": "test fixture",
            "influence_basis": "Test fixture anchor",
            "influence_source": "https://example.com",
        }
        observation = {
            "_location": "test:2",
            "id": "obs-test",
            "record_type": "observation",
            "corpus_layer": "core",
            "source_id": "src-test",
            "behavior": "A1",
            "discourse_position": "where-clause",
            "formula_form": "symbol-or-notation",
            "claim_strength": "definitional",
            "section_role": "notation-or-preliminaries",
            "locator": "fixture",
            "cue": "denotes",
            "summary": "Fixture observation.",
            "quote_words": 0,
        }
        pattern = {
            "_location": "test:3",
            "id": "pat-test",
            "record_type": "pattern",
            "corpus_layer": "core",
            "behavior": "A2",
            "intent": "Fixture pattern.",
            "constructions": ["define ... by ..."],
            "boundaries": ["Fixture boundary."],
            "synthetic_example": "Define x by x:=0.",
            "source_ids": ["src-test"],
            "status": "provisional",
        }

        errors = validate_corpus.validate([source, observation, pattern], [])
        self.assertTrue(any("without a matching observation" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
