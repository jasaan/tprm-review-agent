# Report template

Use these sections, in this order.

```markdown
# Vendor security review: {Vendor} — {product or service}

**Review date:** {YYYY-MM-DD}  **Tier:** {Tier N — label}  **Outcome:** {Approve | Approve with conditions | Escalate | Reject}
**Next review:** {date or months}

## Recommendation
Lead with the decision so a risk owner can act on the first screen:
- The outcome in capitals, with a one-sentence rationale.
- The critical and high findings driving it (up to five).
- What it takes to proceed: each condition with its due date.
- How many questions are open with the vendor and with the requesting team.
- The next review date.

## Summary
Three to five sentences: what the vendor does for us, the tier and why, the most important findings, and the recommended outcome.

## Inherent risk
- Data: ...
- Access: ...
- Criticality: ...
- Tier rationale: ...

## Evidence reviewed
| Document | Type | Notes (period, date, scope) |

## SOC 2 summary
Report type, period, opinion, scope (and whether the purchased product is in scope), exceptions, subservice organizations, CUECs we must operate.

## Control assessment
| Domain | Status | Evidence | NIST CSF 2.0 | NIST 800-53 | ISO 27001 |

## Findings
| ID | Severity | Title | Due (days) |
Then one short section per finding: description, evidence (document + quote), recommendation.

## Contradictions between claims and evidence
| Claim (source) | Contradicting evidence (source) |

## Follow-up questions for the vendor
Numbered, specific, answerable with a document or yes/no.

## Limitations
What this review could not check (documents missing, report period gaps, controls only claimed).
```
