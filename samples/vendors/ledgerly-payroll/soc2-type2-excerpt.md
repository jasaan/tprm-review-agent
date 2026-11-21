# Ledgerly, Inc. — SOC 2 Type II Report (excerpt)

> Fictional sample. Excerpted and abridged for demonstration.

**Period:** July 1, 2025 to June 30, 2026
**Service auditor:** Marrow & Teague CPAs (fictional)
**Trust services criteria:** Security, Availability, Confidentiality

## Section 1 — Independent Service Auditor's Report (abridged)

In our opinion, in all material respects, the description presents Ledgerly's Payroll Platform as designed and implemented throughout the period, and the controls stated in the description were suitably designed and operated effectively throughout the period July 1, 2025 to June 30, 2026.

## Section 3 — Description of the System (abridged)

### Services in scope

Ledgerly Payroll: payroll processing, tax calculation and filing, direct deposit, employee self-service portal, and HR system integrations.

### Subservice organizations

| Subservice organization | Service | Method |
|---|---|---|
| Amazon Web Services (us-east-1, us-east-2) | Infrastructure hosting | Carved out |
| Evergreen Bank, N.A. (fictional) | ACH origination for direct deposit | Carved out |

### Complementary user entity controls (CUECs)

1. User entities are responsible for removing access for their administrators and employees who no longer require it.
2. User entities are responsible for reviewing payroll registers before each payroll run is approved.
3. User entities are responsible for the accuracy of employee data sent from their HR systems.

## Section 4 — Tests of Controls and Results (selected)

| Control | Criterion | Test performed | Result |
|---|---|---|---|
| AC-02: MFA enforced for all workforce and administrative access | CC6.1 | Inspected IdP configuration and a sample of 25 accounts | No exceptions noted |
| AC-05: Quarterly access reviews | CC6.2 | Inspected four quarterly reviews | No exceptions noted |
| VM-01: Independent penetration test annually; findings tracked to closure | CC7.1 | Inspected the test report dated May 6, 2026 and remediation tickets | No exceptions noted |
| LM-03: Security events are centrally logged and alerts triaged 24x7 | CC7.2 | Inspected SIEM configuration and a sample of alerts | No exceptions noted |
| IR-01: Incident response plan maintained and tested annually | CC7.4 | Inspected plan and tabletop record | No exceptions noted |
| BC-02: Daily backups; quarterly restore tests | A1.2 | Inspected backup logs and restore tests | No exceptions noted |
| CH-01: Production changes reviewed and approved | CC8.1 | Inspected a sample of 40 changes | No exceptions noted |
