# Brightpath Analytics, Inc. — SOC 2 Type II Report (excerpt)

> Fictional sample. Excerpted and abridged for demonstration.

**Report on Brightpath Analytics' Description of Its Engagement Platform and on the Suitability of the Design and Operating Effectiveness of Its Controls Relevant to Security and Availability**

**Period:** October 1, 2024 to September 30, 2025
**Service auditor:** Halvorsen & Pike LLP (fictional)

## Section 1 — Independent Service Auditor's Report (abridged)

In our opinion, in all material respects, the description presents Brightpath's Engagement Platform system that was designed and implemented throughout the period October 1, 2024 to September 30, 2025, and the controls stated in the description were suitably designed and operated effectively throughout that period to provide reasonable assurance that Brightpath's service commitments and system requirements were achieved based on the applicable trust services criteria (Security and Availability).

## Section 3 — Description of the System (abridged)

### Services in scope

The **Brightpath Engagement Platform**: appointment reminder messaging (SMS and email), patient survey tools and the reporting dashboard.

### Services not in scope

The following are **excluded** from this report: the **Insights ML** predictive analytics module (general availability April 2025) and the Brightpath mobile SDK.

### Subservice organizations

| Subservice organization | Service | Method |
|---|---|---|
| Amazon Web Services (us-east-1, us-west-2) | Infrastructure hosting | Carved out |
| Twilio | SMS delivery | Carved out |
| Northwind Data Labeling (Manila, Philippines) | Annotation of de-identified and limited data sets used to improve predictive models | Carved out |

### Complementary user entity controls (CUECs)

1. User entities are responsible for managing their own users' access to the Brightpath dashboard, including timely removal of departed users.
2. User entities are responsible for configuring SSO and enforcing MFA through their identity provider.
3. User entities are responsible for ensuring data sent to Brightpath is limited to what is necessary for the service.

## Section 4 — Tests of Controls and Results (selected)

| Control | Criterion | Test performed | Result |
|---|---|---|---|
| CA-04: Production administrative access requires MFA | CC6.1 | Inspected MFA configuration for a sample of 25 production administrator accounts | **Exception noted.** 3 of 25 sampled administrator accounts did not have MFA enforced during the period. |
| CA-09: Access is removed within 3 business days of termination | CC6.2 | Inspected deprovisioning for a sample of 15 terminated employees | No exceptions noted |
| VM-02: An independent penetration test is performed annually | CC7.1 | Inspected the most recent penetration test report | No exceptions noted. Most recent test dated **March 14, 2024**. |
| IR-01: An incident response plan is maintained and tested annually | CC7.4 | Inspected the plan and tabletop exercise records | No exceptions noted |
| BC-03: Backups are performed daily and restoration is tested annually | A1.2 | Inspected backup logs and restore test record | No exceptions noted |

**Management's response to CA-04 exception:** The three accounts were legacy service administrator accounts. MFA was enforced on these accounts in November 2025, after the period.
