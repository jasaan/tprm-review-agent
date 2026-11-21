"""Score an agent's findings.json against the answer key for a sample vendor.

Usage:
    python evals/score.py output/brightpath-analytics/findings.json evals/expected/brightpath-analytics.json
    python evals/score.py --all            # score every vendor that has output
    python evals/score.py --self-test      # check the scorer itself, no API needed

The checks are deliberately simple and transparent: tier and outcome must be in the
accepted set, each planted issue must appear (keyword match in findings or
contradictions, and/or a specific field value), and things that should NOT be
flagged must be absent. Keyword matching can miss a correct finding phrased in an
unexpected way, so read the report when a check fails before blaming the agent.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent


def _get(data: dict, dotted: str):
    for key in dotted.split("."):
        data = data[key]
    return data


def _section_text(review: dict, section: str | None) -> str:
    if section == "contradictions":
        items = review["contradictions"]
    elif section == "challenge_log":
        items = review.get("challenge_log", []) + [{"q": q} for q in review.get("questions_for_requesting_team", [])]
    else:
        items = review["findings"] + review["contradictions"]
    return " ".join(json.dumps(item) for item in items).lower()


def score(review: dict, key: dict) -> tuple[int, int, list[str]]:
    lines: list[str] = []
    passed = total = 0

    def check(ok: bool, label: str) -> None:
        nonlocal passed, total
        total += 1
        passed += ok
        lines.append(f"  {'PASS' if ok else 'FAIL'}  {label}")

    tier = review["inherent_risk"]["tier"]
    check(tier in key["expected_tier"], f"tier {tier!r} in {key['expected_tier']}")
    outcome = review["outcome"]
    check(outcome in key["acceptable_outcomes"], f"outcome {outcome!r} in {key['acceptable_outcomes']}")

    for item in key["must_find"]:
        ok = True
        if item.get("match_any"):
            text = _section_text(review, item.get("section"))
            ok = any(term.lower() in text for term in item["match_any"])
        if "check_field" in item:
            ok = ok and _get(review, item["check_field"]) == item["expect_value"]
        check(ok, f"{item['id']} found: {item['description']}")

    for item in key.get("must_not_find", []):
        ok = True
        if "max_severity_count" in item:
            for sev, limit in item["max_severity_count"].items():
                ok = ok and sum(f["severity"] == sev for f in review["findings"]) <= limit
        if item.get("match_any"):
            text = _section_text(review, item.get("section"))
            ok = ok and not any(term.lower() in text for term in item["match_any"])
        check(ok, f"{item['id']} absent: {item['description']}")

    if "min_challenges" in key:
        n = len(review.get("challenge_log", []))
        check(n >= key["min_challenges"], f"skeptic raised {n} challenge(s), minimum {key['min_challenges']}")
        unresolved = [c for c in review.get("challenge_log", []) if not c.get("response", "").strip()]
        check(not unresolved, "every challenge has a written resolution")

    return passed, total, lines


def score_files(findings_path: Path, key_path: Path) -> bool:
    review = json.loads(findings_path.read_text(encoding="utf-8"))
    key = json.loads(key_path.read_text(encoding="utf-8"))
    passed, total, lines = score(review, key)
    print(f"{key['vendor']}: {passed}/{total} checks passed")
    print("\n".join(lines))
    return passed == total


def self_test() -> None:
    """A hand-built review that should pass the Ledgerly key, and a broken one that shouldn't."""
    key = json.loads((REPO / "evals/expected/ledgerly-payroll.json").read_text(encoding="utf-8"))
    good = {
        "inherent_risk": {"tier": "Tier 2"},
        "outcome": "approve",
        "soc2": {"purchased_product_in_scope": True},
        "findings": [{"severity": "low", "title": "Retention period after termination"}],
        "contradictions": [],
        "challenge_log": [
            {"challenge_id": "C1", "target": "vendor", "challenge": "RPO vs backup cadence",
             "resolution": "needs_answer", "response": "Asked the vendor for backup frequency evidence."}
        ],
    }
    bad = dict(good, outcome="reject", contradictions=[{"claim": "MFA for all users"}])
    assert score(good, key)[0] == score(good, key)[1], "good review should pass every check"
    passed, total, _ = score(bad, key)
    assert passed == total - 2, f"bad review should fail exactly 2 checks, failed {total - passed}"
    print("self-test passed")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("findings", nargs="?", type=Path)
    parser.add_argument("key", nargs="?", type=Path)
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        self_test()
        return
    if args.all:
        results = []
        for key_path in sorted((REPO / "evals/expected").glob("*.json")):
            findings = REPO / "output" / key_path.stem / "findings.json"
            if findings.exists():
                results.append(score_files(findings, key_path))
            else:
                print(f"{key_path.stem}: no output yet (run agent/review.py samples/vendors/{key_path.stem})")
        sys.exit(0 if results and all(results) else 1)
    if not (args.findings and args.key):
        parser.error("give a findings.json and an answer key, or use --all / --self-test")
    sys.exit(0 if score_files(args.findings, args.key) else 1)


if __name__ == "__main__":
    main()
