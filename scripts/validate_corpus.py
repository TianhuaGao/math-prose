#!/usr/bin/env python3
"""Validate a Math Prose JSONL corpus using only the Python standard library."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Iterable


BEHAVIORS = {
    "A0", "A1", "A2", "A3", "A4", "A5",
    "B1", "B2", "B3", "B4", "B5", "B6",
    "C1", "C2", "C3", "C4", "C5",
    "D1", "D2", "D3", "D4", "D5",
    "E1", "E2", "E3", "E4", "E5",
    "F1", "F2", "F3", "F4",
}

DISCIPLINES = {
    "pure-mathematics",
    "applied-mathematics",
    "probability-statistics",
    "optimization-machine-learning",
    "control-robotics",
    "physics-engineering",
}

SOURCE_ROLES = {"anchor", "comparison"}

DISCOURSE_POSITIONS = {
    "before-display",
    "display-lead",
    "where-clause",
    "after-display",
    "derivation-step",
    "result-statement",
    "proof-step",
    "paragraph-transition",
}

FORMULA_FORMS = {
    "symbol-or-notation",
    "definition",
    "equality-or-identity",
    "membership-or-signature",
    "mapping-or-transform",
    "differential-equation",
    "recurrence-or-update",
    "optimization",
    "inequality-or-bound",
    "limit-or-asymptotic",
    "integral-or-sum",
    "piecewise-or-cases",
    "probability-or-expectation",
    "theorem-or-proposition",
    "algorithmic-relation",
}

CLAIM_STRENGTHS = {
    "descriptive",
    "definitional",
    "exact-algebraic",
    "approximate",
    "one-way-consequence",
    "equivalence",
    "proved-result",
    "empirical-observation",
}

SECTION_ROLES = {
    "notation-or-preliminaries",
    "problem-formulation",
    "method-or-model",
    "derivation-or-analysis",
    "theorem-or-proof",
    "algorithm",
    "experiment-or-results",
    "discussion-or-limitations",
    "appendix",
}

STATUSES = {"seed", "provisional", "validated"}

REQUIRED = {
    "source": {
        "id", "record_type", "source_role", "title", "year", "discipline",
        "citation", "access",
    },
    "observation": {
        "id", "record_type", "source_id", "behavior", "discourse_position",
        "formula_form", "claim_strength", "section_role", "locator", "cue",
        "summary", "quote_words",
    },
    "pattern": {
        "id", "record_type", "behavior", "intent", "constructions",
        "boundaries", "synthetic_example", "source_ids", "status",
    },
}


def read_jsonl(path: str) -> tuple[list[dict[str, Any]], list[str]]:
    stream = sys.stdin if path == "-" else Path(path).open("r", encoding="utf-8")
    records: list[dict[str, Any]] = []
    errors: list[str] = []
    try:
        for line_number, raw_line in enumerate(stream, start=1):
            line = raw_line.strip()
            if not line or line.startswith("#"):
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                errors.append(f"line {line_number}: invalid JSON: {exc.msg}")
                continue
            if not isinstance(record, dict):
                errors.append(f"line {line_number}: each record must be a JSON object")
                continue
            record["_line"] = line_number
            records.append(record)
    finally:
        if stream is not sys.stdin:
            stream.close()
    return records, errors


def require_string_list(record: dict[str, Any], field: str, errors: list[str]) -> None:
    value = record.get(field)
    if not isinstance(value, list) or not all(isinstance(item, str) and item.strip() for item in value):
        errors.append(f"line {record['_line']}: {field} must be a list of non-empty strings")


def require_non_empty_string(record: dict[str, Any], field: str, errors: list[str]) -> None:
    value = record.get(field)
    if not isinstance(value, str) or not value.strip():
        errors.append(f"line {record['_line']}: {field} must be a non-empty string")


def check_enum(record: dict[str, Any], field: str, allowed: set[str], errors: list[str]) -> None:
    if record.get(field) not in allowed:
        errors.append(
            f"line {record['_line']}: unsupported {field}={record.get(field)!r}; "
            f"expected one of {sorted(allowed)}"
        )


def validate(records: Iterable[dict[str, Any]], initial_errors: list[str]) -> list[str]:
    records = list(records)
    errors = list(initial_errors)
    ids: dict[str, int] = {}
    sources: dict[str, dict[str, Any]] = {}

    for record in records:
        line = record["_line"]
        record_type = record.get("record_type")
        if record_type not in REQUIRED:
            errors.append(f"line {line}: record_type must be source, observation, or pattern")
            continue
        missing = sorted(REQUIRED[record_type] - record.keys())
        if missing:
            errors.append(f"line {line}: missing required fields: {', '.join(missing)}")
        record_id = record.get("id")
        if not isinstance(record_id, str) or not record_id.strip():
            errors.append(f"line {line}: id must be a non-empty string")
        elif record_id in ids:
            errors.append(f"line {line}: duplicate id {record_id!r}; first used on line {ids[record_id]}")
        else:
            ids[record_id] = line
            if record_type == "source":
                sources[record_id] = record

    for record in records:
        record_type = record.get("record_type")
        if record_type not in REQUIRED:
            continue
        if record_type == "source":
            check_enum(record, "source_role", SOURCE_ROLES, errors)
            check_enum(record, "discipline", DISCIPLINES, errors)
            year = record.get("year")
            if not isinstance(year, int) or year < 1500 or year > 2100:
                errors.append(f"line {record['_line']}: year must be an integer from 1500 to 2100")
            if record.get("source_role") == "anchor":
                require_non_empty_string(record, "influence_basis", errors)
                require_non_empty_string(record, "influence_source", errors)

        elif record_type == "observation":
            check_enum(record, "behavior", BEHAVIORS, errors)
            check_enum(record, "discourse_position", DISCOURSE_POSITIONS, errors)
            check_enum(record, "formula_form", FORMULA_FORMS, errors)
            check_enum(record, "claim_strength", CLAIM_STRENGTHS, errors)
            check_enum(record, "section_role", SECTION_ROLES, errors)
            if record.get("source_id") not in sources:
                errors.append(f"line {record['_line']}: unknown source_id {record.get('source_id')!r}")
            quote = record.get("quote", "")
            quote_words = record.get("quote_words")
            if not isinstance(quote_words, int) or quote_words < 0:
                errors.append(f"line {record['_line']}: quote_words must be a non-negative integer")
            elif quote_words > 25:
                errors.append(f"line {record['_line']}: public-corpus quote exceeds 25 words")
            if quote:
                actual_words = len(str(quote).split())
                if quote_words != actual_words:
                    errors.append(
                        f"line {record['_line']}: quote_words={quote_words} but quote contains {actual_words} words"
                    )

        elif record_type == "pattern":
            check_enum(record, "behavior", BEHAVIORS, errors)
            check_enum(record, "status", STATUSES, errors)
            require_string_list(record, "constructions", errors)
            require_string_list(record, "boundaries", errors)
            require_string_list(record, "source_ids", errors)
            source_ids = record.get("source_ids", [])
            if isinstance(source_ids, list):
                unknown = sorted(source_id for source_id in source_ids if source_id not in sources)
                if unknown:
                    errors.append(f"line {record['_line']}: unknown source_ids: {', '.join(unknown)}")
                anchor_source_ids = {
                    source_id for source_id in source_ids
                    if source_id in sources and sources[source_id].get("source_role") == "anchor"
                }
                if record.get("status") == "validated" and len(anchor_source_ids) < 3:
                    errors.append(
                        f"line {record['_line']}: validated patterns require at least three independent anchor sources"
                    )
                if record.get("status") == "provisional" and not anchor_source_ids:
                    errors.append(
                        f"line {record['_line']}: provisional patterns require at least one anchor source"
                    )

    return errors


def summarize(records: Iterable[dict[str, Any]]) -> str:
    records = list(records)
    types = Counter(record.get("record_type", "unknown") for record in records)
    behaviors = Counter(record.get("behavior") for record in records if record.get("behavior"))
    disciplines = Counter(
        record.get("discipline") for record in records
        if record.get("record_type") == "source" and record.get("discipline")
    )
    source_roles = Counter(
        record.get("source_role") for record in records
        if record.get("record_type") == "source" and record.get("source_role")
    )
    section_roles = Counter(
        record.get("section_role") for record in records
        if record.get("record_type") == "observation" and record.get("section_role")
    )
    statuses = Counter(
        record.get("status") for record in records
        if record.get("record_type") == "pattern" and record.get("status")
    )
    type_summary = ", ".join(f"{key}={value}" for key, value in sorted(types.items())) or "none"
    behavior_summary = ", ".join(f"{key}={value}" for key, value in sorted(behaviors.items())) or "none"
    discipline_summary = ", ".join(
        f"{key}={value}" for key, value in sorted(disciplines.items())
    ) or "none"
    source_role_summary = ", ".join(
        f"{key}={value}" for key, value in sorted(source_roles.items())
    ) or "none"
    section_summary = ", ".join(
        f"{key}={value}" for key, value in sorted(section_roles.items())
    ) or "none"
    status_summary = ", ".join(
        f"{key}={value}" for key, value in sorted(statuses.items())
    ) or "none"
    return (
        f"records: {type_summary}\n"
        f"behaviors: {behavior_summary}\n"
        f"source_roles: {source_role_summary}\n"
        f"disciplines: {discipline_summary}\n"
        f"section_roles: {section_summary}\n"
        f"pattern_statuses: {status_summary}"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("corpus", help="JSONL corpus path, or - for standard input")
    args = parser.parse_args()

    records, parse_errors = read_jsonl(args.corpus)
    errors = validate(records, parse_errors)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"FAIL: {len(errors)} validation error(s)", file=sys.stderr)
        return 1

    print("PASS")
    print(summarize(records))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
