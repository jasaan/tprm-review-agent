# Risk tiering, severity and cadence

## Inherent-risk tier

Decide from the intake note, before reading vendor evidence. Take the **highest** tier any single factor points to.

| Factor | Tier 1 — Critical | Tier 2 — High | Tier 3 — Moderate | Tier 4 — Low |
|---|---|---|---|---|
| Data the vendor stores or processes | Regulated health data (PHI), payment card data, credentials or keys, large volumes of sensitive personal data | Personal data (employee or customer PII), financial records, confidential business data | Internal, non-sensitive business data | Public data only, or no company data |
| Access to our environment | Privileged or administrative access, code running inside our network, direct database access | Integration with core systems (SSO, HR, finance, production APIs) with write access | Read-only integration or limited user accounts | No integration |
| Business criticality | Outage stops a critical business process or patient/customer service | Outage disrupts an important process; workaround exists | Outage is an inconvenience | No operational impact |

## Review depth and cadence by tier

| Tier | Evidence expected | Re-review |
|---|---|---|
| Tier 1 | SOC 2 Type II (or ISO 27001 certificate with Statement of Applicability) covering the product, pen test summary under 12 months old, full questionnaire, contract security and breach terms, BAA/DPA where applicable | Every 12 months, plus continuous monitoring of breaches and attack surface |
| Tier 2 | SOC 2 Type II or ISO 27001, questionnaire, contract breach terms | Every 12 months |
| Tier 3 | Questionnaire or trust-center review | Every 24 months |
| Tier 4 | Intake note only | At onboarding; again if the use changes |

## Finding severity

| Severity | Meaning | Examples | Remediation due |
|---|---|---|---|
| Critical | Likely exposure of sensitive data or our environment, or a mandatory requirement can't be met | No MFA on production admin access with PHI; refuses to sign a BAA; known unremediated breach | 30 days, or block until fixed |
| High | A significant control gap or contradiction in a Tier 1–2 vendor | SOC 2 exception on a key control; product not in SOC 2 scope; undisclosed subprocessor; claim contradicted by evidence | 60 days |
| Medium | A gap with compensating controls or limited blast radius | Pen test older than 12 months; vague breach-notification timing; backup restores not tested | 90 days |
| Low | Hygiene or documentation issue | Missing bridge letter for a recent report period; policy review overdue | Track at next review |

## Outcome guide

| Situation | Outcome |
|---|---|
| No critical or high findings | Approve |
| High findings with a credible fix, or several mediums | Approve with conditions |
| Any critical finding, or high findings in a Tier 1 vendor without a committed fix | Escalate to a named risk owner |
| A mandatory requirement can't be met | Reject |
