"""Load the control catalog (the Markdown table in the skill) as data.

The model only names a domain; the NIST and ISO mappings in the report come from
this table, so the report can't contain a control ID the catalog doesn't list.
"""

from __future__ import annotations

from pathlib import Path

CATALOG = Path(__file__).resolve().parent.parent / "skills/vendor-security-review/references/control-catalog.md"


def _split(cell: str) -> list[str]:
    return [part.strip() for part in cell.split(",") if part.strip()]


def load_catalog() -> dict[str, dict[str, list[str]]]:
    rows: dict[str, dict[str, list[str]]] = {}
    for line in CATALOG.read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 6 or not cells[0].isdigit():
            continue  # header, separator or prose
        _, domain, _evidence, csf, sp80053, iso = cells
        rows[domain] = {"nist_csf": _split(csf), "nist_800_53": _split(sp80053), "iso_27001": _split(iso)}
    if len(rows) != 12:
        raise RuntimeError(f"Expected 12 domains in {CATALOG.name}, found {len(rows)}")
    return rows


MAPPINGS = load_catalog()
DOMAINS = list(MAPPINGS)


def add_mappings(review) -> None:
    """Fill each control's domain name and framework mappings from the catalog."""
    for control in review.controls:
        if not 1 <= control.domain_id <= len(DOMAINS):
            raise ValueError(f"Control domain_id {control.domain_id} is not in the catalog (1-{len(DOMAINS)})")
        control.domain = DOMAINS[control.domain_id - 1]
        m = MAPPINGS[control.domain]
        control.nist_csf, control.nist_800_53, control.iso_27001 = m["nist_csf"], m["nist_800_53"], m["iso_27001"]
