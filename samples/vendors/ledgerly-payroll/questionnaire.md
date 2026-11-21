# Ledgerly — Security Questionnaire (CAIQ-style, abridged)

> Fictional sample. Completed by: P. Okafor, Security Lead (fictional). Date: September 18, 2026.

| # | Question | Vendor answer |
|---|---|---|
| IAM-1 | Is MFA enforced for all workforce and administrative access to production? | Yes, enforced through our IdP for all workforce accounts; see SOC 2 control AC-02. |
| IAM-2 | Do you support SAML SSO for customer users? | Yes, SAML 2.0 and SCIM provisioning. |
| DAT-1 | Is customer data encrypted in transit and at rest? | Yes. TLS 1.2+ in transit; AES-256 at rest with AWS KMS; bank account numbers additionally encrypted at the field level. |
| DAT-2 | In which countries is customer data stored or processed? | United States only (AWS us-east-1 and us-east-2). Support staff are US-based. |
| SUB-1 | List all subprocessors with access to customer data. | AWS (hosting), Evergreen Bank (ACH). Current list at ledgerly.example/subprocessors with 30 days' notice of changes. |
| VUL-1 | When was your last independent penetration test? | May 2026, by an independent firm. Executive summary attached to this questionnaire. |
| VUL-2 | What are your remediation timelines for critical vulnerabilities? | Critical 7 days, high 30 days, medium 90 days. |
| INC-1 | How quickly will you notify customers of a security incident affecting their data? | Within 72 hours of confirmation, per Section 9 of our DPA. |
| BCP-1 | What are your RTO and RPO? | RTO 8 hours, RPO 1 hour; tested quarterly. |
| PRV-1 | Do you use customer data to train or improve machine learning models? | No. Customer data is not used for model training. |
| PRV-2 | Will you return or delete customer data at contract termination? | Yes. Export available on request; deletion within 30 days after the end of the legally required retention period for payroll tax records (generally 4 years under IRS rules). |
| AUD-1 | Do you hold a current SOC 2 Type II report covering all products? | Yes, July 2025 to June 2026, covering Ledgerly Payroll. |
