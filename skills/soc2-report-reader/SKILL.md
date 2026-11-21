---
name: soc2-report-reader
description: Extract what a third-party risk reviewer needs from a SOC 2 report (Type I or Type II), whole or excerpted: report type, audit period, service auditor's opinion, system description and scope, in-scope and carved-out products and subservice organizations, testing exceptions and management responses, and complementary user entity controls (CUECs). Use when reading a SOC 2 or SOC 1 report, or a vendor's audit report, as part of a vendor review.
---

# SOC 2 report reader

SOC 2 reports are long, and most of the value is in a few places. Pull these out, quote briefly, and cite the section.

## What to extract

1. **Report type**: Type I (design at a point in time) or Type II (design and operating effectiveness over a period). Type I is much weaker evidence; say so.
2. **Audit period**: start and end dates. If the period ended more than 6 months before the review date, note that a **bridge letter** should be requested.
3. **Opinion** (Section 1, the independent service auditor's report):
   - Unqualified: controls suitably designed and operating effectively.
   - Qualified: one or more criteria not met. Quote the qualification.
   - Adverse or disclaimer: treat as a critical finding.
4. **Scope** (Section 3, system description): which products, services, locations and Trust Services Criteria (security, availability, confidentiality, processing integrity, privacy) are covered. List anything explicitly **excluded**.
5. **Subservice organizations**: who they are, what they do, and whether they are included (inclusive method) or carved out. Carved-out subservice organizations are not tested; their controls are the vendor's responsibility to monitor.
6. **Exceptions** (Section 4, tests of controls): for each exception, the control, the criterion (for example CC6.1), what was found, the sample size, and management's response. Exceptions on access control (CC6.x), change management (CC8.1) or incident response (CC7.x) deserve particular attention.
7. **CUECs**: controls the customer (us) must operate for the vendor's controls to work, such as managing our own user access or reviewing audit logs. These become our obligations.

## How to judge it

- An unqualified opinion with exceptions is common. The exceptions still matter.
- A management response that says "remediated after the period" is a claim; ask for evidence.
- If the product being purchased isn't in the system description, the report says little about that product.
- If key subservice organizations (for example a data-labeling firm or a support outsourcer) are carved out, the data they handle is outside the auditor's testing.

## Output

A short structured summary: type, period, opinion, scope (in and out), subservice organizations (included or carved out, location if stated), exceptions (control, criterion, finding, management response), CUECs, and any bridge-letter need.
