"""Output schema for a vendor security review.

REVIEW_SCHEMA is sent to the Claude API as a structured-output JSON schema, so the
model's reply is guaranteed to parse. The Pydantic models mirror it and validate the
reply again on our side before anything is written to disk.
"""

from __future__ import annotations

from typing import List, Literal

from pydantic import BaseModel


Status = Literal["met", "partially_met", "not_met", "not_evidenced"]
Severity = Literal["critical", "high", "medium", "low"]
Outcome = Literal["approve", "approve_with_conditions", "escalate", "reject"]
Tier = Literal["Tier 1", "Tier 2", "Tier 3", "Tier 4"]


class InherentRisk(BaseModel):
    data_types: List[str]
    access_level: str
    criticality: str
    tier: Tier
    rationale: str


class Soc2Summary(BaseModel):
    present: bool
    report_type: str
    period: str
    opinion: str
    purchased_product_in_scope: bool
    scope_notes: str
    exceptions: List[str]
    subservice_orgs: List[str]
    cuecs: List[str]
    bridge_letter_needed: bool


class Control(BaseModel):
    domain_id: int  # 1-12, the row number in the control catalog
    domain: str = ""  # filled in from the catalog
    status: Status
    evidence: str
    # Filled in by agent/catalog.py from the control catalog, never by the model.
    nist_csf: List[str] = []
    nist_800_53: List[str] = []
    iso_27001: List[str] = []


class Finding(BaseModel):
    id: str
    title: str
    severity: Severity
    domain: str
    description: str
    evidence: str
    source_documents: List[str]
    recommendation: str
    remediation_due_days: int


class Contradiction(BaseModel):
    claim: str
    claim_source: str
    contradicting_evidence: str
    evidence_source: str


Target = Literal["intake", "vendor", "review"]
Ask = Literal["requesting_team", "vendor", "reviewer"]
Change = Literal[
    "none", "add_finding", "raise_severity", "lower_severity",
    "remove_finding", "change_status", "change_tier", "change_outcome",
]
Resolution = Literal["accepted", "rejected", "needs_answer"]


class Challenge(BaseModel):
    id: str
    target: Target
    refers_to: str
    challenge: str
    why_it_matters: str
    ask: Ask
    question: str
    proposed_change: Change


class Challenges(BaseModel):
    challenges: List[Challenge]


class ChallengeResolution(BaseModel):
    challenge_id: str
    target: Target
    challenge: str
    resolution: Resolution
    response: str


class Resolutions(BaseModel):
    questions_for_requesting_team: List[str]
    challenge_log: List["ChallengeResolution"]


class Review(BaseModel):
    vendor_name: str
    product_or_service: str
    review_date: str
    summary: str
    inherent_risk: InherentRisk
    documents_reviewed: List[str]
    soc2: Soc2Summary
    controls: List[Control]
    findings: List[Finding]
    contradictions: List[Contradiction]
    outcome: Outcome
    outcome_rationale: str
    conditions: List[str]
    follow_up_questions: List[str]
    next_review_months: int
    limitations: List[str]
    questions_for_requesting_team: List[str] = []
    challenge_log: List[ChallengeResolution] = []


def _obj(properties: dict) -> dict:
    """A strict JSON-schema object: every property required, nothing extra allowed."""
    return {
        "type": "object",
        "properties": properties,
        "required": list(properties),
        "additionalProperties": False,
    }


_STR = {"type": "string"}
_INT = {"type": "integer"}
_BOOL = {"type": "boolean"}
_STRS = {"type": "array", "items": _STR}


def _enum(*values: str) -> dict:
    return {"type": "string", "enum": list(values)}


_TARGET = _enum("intake", "vendor", "review")


REVIEW_SCHEMA = _obj(
    {
        "vendor_name": _STR,
        "product_or_service": _STR,
        "review_date": _STR,
        "summary": _STR,
        "inherent_risk": _obj(
            {
                "data_types": _STRS,
                "access_level": _STR,
                "criticality": _STR,
                "tier": _enum("Tier 1", "Tier 2", "Tier 3", "Tier 4"),
                "rationale": _STR,
            }
        ),
        "documents_reviewed": _STRS,
        "soc2": _obj(
            {
                "present": _BOOL,
                "report_type": _STR,
                "period": _STR,
                "opinion": _STR,
                "purchased_product_in_scope": _BOOL,
                "scope_notes": _STR,
                "exceptions": _STRS,
                "subservice_orgs": _STRS,
                "cuecs": _STRS,
                "bridge_letter_needed": _BOOL,
            }
        ),
        "controls": {
            "type": "array",
            "items": _obj(
                {
                    "domain_id": _INT,
                    "status": _enum("met", "partially_met", "not_met", "not_evidenced"),
                    "evidence": _STR,
                }
            ),
        },
        "findings": {
            "type": "array",
            "items": _obj(
                {
                    "id": _STR,
                    "title": _STR,
                    "severity": _enum("critical", "high", "medium", "low"),
                    "domain": _STR,
                    "description": _STR,
                    "evidence": _STR,
                    "source_documents": _STRS,
                    "recommendation": _STR,
                    "remediation_due_days": _INT,
                }
            ),
        },
        "contradictions": {
            "type": "array",
            "items": _obj(
                {
                    "claim": _STR,
                    "claim_source": _STR,
                    "contradicting_evidence": _STR,
                    "evidence_source": _STR,
                }
            ),
        },
        "outcome": _enum("approve", "approve_with_conditions", "escalate", "reject"),
        "outcome_rationale": _STR,
        "conditions": _STRS,
        "follow_up_questions": _STRS,
        "next_review_months": _INT,
        "limitations": _STRS,
    }
)

RESOLUTION_SCHEMA = _obj(
    {
        "questions_for_requesting_team": _STRS,
        "challenge_log": {
            "type": "array",
            "items": _obj(
                {
                    "challenge_id": _STR,
                    "target": _TARGET,
                    "challenge": _STR,
                    "resolution": _enum("accepted", "rejected", "needs_answer"),
                    "response": _STR,
                }
            ),
        },
    }
)

CHALLENGE_SCHEMA = _obj(
    {
        "challenges": {
            "type": "array",
            "items": _obj(
                {
                    "id": _STR,
                    "target": _TARGET,
                    "refers_to": _STR,
                    "challenge": _STR,
                    "why_it_matters": _STR,
                    "ask": _enum("requesting_team", "vendor", "reviewer"),
                    "question": _STR,
                    "proposed_change": _enum(
                        "none", "add_finding", "raise_severity", "lower_severity",
                        "remove_finding", "change_status", "change_tier", "change_outcome",
                    ),
                }
            ),
        }
    }
)
