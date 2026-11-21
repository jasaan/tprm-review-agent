---
name: questionnaire-gap-check
description: Compare a vendor's security questionnaire answers (SIG Lite, CAIQ, or a custom questionnaire) and marketing or trust-center claims against independent evidence such as a SOC 2 report, pen test letter or contract, and flag every claim the evidence contradicts, every important claim with no evidence behind it, and every evasive answer. Use during a vendor review, or when asked whether a vendor's answers can be trusted.
---

# Questionnaire gap check

Questionnaires are self-reported. The job here is to find where self-reporting and evidence disagree.

## Procedure

1. **List the material claims.** From the questionnaire and any security overview, list claims about: MFA and admin access, encryption, data location and residency, subprocessors, pen testing date, vulnerability SLAs, logging and monitoring, incident notification timing, backups and RTO/RPO, data retention and deletion, and use of customer data for AI or analytics.
2. **Find the evidence for each.** Look in the SOC 2 report (system description, subservice organizations, tests and exceptions), pen test letter, contract or DPA, and the intake note.
3. **Classify each claim:**
   - `supported`: independent evidence agrees.
   - `contradicted`: independent evidence disagrees. Always a finding.
   - `unsupported`: no independent evidence. Becomes a follow-up question; becomes a finding if the claim is important for this vendor's tier.
   - `evasive`: the answer doesn't address the question (for example "we follow industry best practices" to a yes/no question on MFA). Becomes a follow-up question.

## Typical contradictions to look for

- "MFA is enforced for all users" vs a SOC 2 exception on MFA for admins.
- "Customer data never leaves the United States" vs a subservice organization or support team in another country.
- "Annual third-party penetration testing" vs a pen test letter dated more than 12 months ago.
- "We notify customers of breaches within 24 hours" vs contract language that says "without undue delay".
- "We do not use customer data to train models" vs terms of service or a DPA that allow it unless the customer opts out.

## Output

A table of claim, source, evidence, source, classification. List contradictions first. Quote both sides briefly so a reader can verify each one without reopening the documents.
