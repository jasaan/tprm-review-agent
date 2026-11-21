# Control catalog

Twelve domains, condensed from the structure of public questionnaires (Shared Assessments SIG Lite and the CSA Consensus Assessments Initiative Questionnaire) and mapped to NIST CSF 2.0, NIST SP 800-53 Rev. 5 and ISO/IEC 27001:2022 Annex A. The mappings are indicative, to help readers cross-reference; check them against the official framework documents before relying on them for an audit.

| # | Domain | What good evidence looks like | NIST CSF 2.0 | NIST SP 800-53 Rev. 5 | ISO/IEC 27001:2022 Annex A |
|---|---|---|---|---|---|
| 1 | Governance and policy | Approved, current security policy set; named security owner | GV.PO-01, GV.RR-02 | PL-1, PM-2 | 5.1, 5.2 |
| 2 | Supply chain and subprocessors | Complete subprocessor list with locations; flow-down of security terms; monitoring of their own vendors | GV.SC-05, GV.SC-07 | SA-9, SR-3, SR-6 | 5.19, 5.20, 5.21, 5.22 |
| 3 | Identity and access management | SSO, MFA enforced for all users and especially admins, least privilege, timely deprovisioning, periodic access reviews | PR.AA-01, PR.AA-03, PR.AA-05 | AC-2, AC-6, IA-2(1) | 5.15, 5.17, 5.18, 8.2, 8.5 |
| 4 | Data protection and encryption | Encryption in transit (TLS 1.2+) and at rest; key management; data segregation between customers | PR.DS-01, PR.DS-02 | SC-8, SC-12, SC-28 | 8.24, 5.34 |
| 5 | Logging and monitoring | Centralized security logging, alerting, retention; 24x7 monitoring for critical systems | DE.CM-01, DE.CM-09 | AU-2, AU-6, SI-4 | 8.15, 8.16 |
| 6 | Vulnerability management and testing | Regular scanning, defined patch SLAs, independent pen test within 12 months with remediation tracking | ID.RA-01, PR.PS-02 | RA-5, CA-8 | 8.8 |
| 7 | Secure development | SDLC with code review, security testing in CI, dependency management, change control | PR.PS-06 | SA-11, SA-15 | 8.25, 8.28, 8.29 |
| 8 | Incident response and breach notification | Tested IR plan; contractual notice to customers within a defined time (for example 72 hours); named contact | RS.MA-01, RS.CO-02 | IR-4, IR-6, IR-8 | 5.24, 5.26 |
| 9 | Business continuity and backup | Documented RTO/RPO, backups tested by restore, BC/DR plan exercised | PR.DS-11, RC.RP-01 | CP-2, CP-9, CP-10 | 5.29, 5.30, 8.13 |
| 10 | Privacy and data handling | Data location, retention and deletion on termination; lawful basis; BAA/DPA where required | GV.OC-03 | PT-2, SI-12 | 5.31, 5.34, 8.10 |
| 11 | Personnel security and training | Background checks, security awareness training, confidentiality agreements | PR.AT-01 | AT-2, PS-3 | 6.1, 6.2, 6.3 |
| 12 | AI and automated processing | Whether customer data trains models, opt-out terms, model and data provenance, human oversight of automated decisions | GV.SC-05 (contract terms); see also NIST AI RMF (Map, Measure) | SA-9, PT-2 | 5.20, 5.34; see also ISO/IEC 42001 |

## Notes for reviewers

- Domains 2, 8, 10 and 12 often live in the **contract**, not the SOC 2 report. If there is no contract or DPA in the evidence, mark them `not_evidenced` and ask.
- A SOC 2 control with an exception is `partially_met` at best, even if the vendor says it's fixed. Ask for evidence of the fix.
- For AI tools, check domain 12 even if the vendor isn't marketed as "AI": many SaaS products now use customer data for model training by default.
