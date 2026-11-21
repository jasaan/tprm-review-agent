# Brightpath Analytics — Security Questionnaire (SIG Lite–style, abridged)

> Fictional sample. Completed by: J. Ramos, Director of Compliance (fictional). Date: October 2, 2026.

| # | Question | Vendor answer |
|---|---|---|
| IAM-1 | Is MFA enforced for all workforce and administrative access to production? | Yes. MFA is enforced for all users without exception. |
| IAM-2 | Do you support SAML SSO for customer users? | Yes. |
| DAT-1 | Is customer data encrypted in transit and at rest? | Yes. TLS 1.2+ in transit; AES-256 at rest using AWS KMS. |
| DAT-2 | In which countries is customer data stored or processed? | United States only. Customer data never leaves the US. |
| SUB-1 | List all subprocessors with access to customer data. | AWS (hosting), Twilio (SMS). |
| VUL-1 | When was your last independent penetration test? | We perform annual third-party penetration testing. Summary available under NDA. |
| VUL-2 | What are your remediation timelines for critical vulnerabilities? | We follow industry best practices. |
| INC-1 | How quickly will you notify customers of a security incident affecting their data? | Without undue delay, consistent with applicable law. |
| BCP-1 | What are your RTO and RPO for the Insights ML module? | RTO 72 hours, RPO 24 hours. |
| PRV-1 | Do you use customer data to train or improve machine learning models? | We use aggregated data to improve our services. |
| PRV-2 | Will you return or delete customer data at contract termination? | Yes, on request. |
| AUD-1 | Do you hold a current SOC 2 Type II report covering all products? | Yes. |
