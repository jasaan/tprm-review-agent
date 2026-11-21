# claude-security-skills

**Claude skills and an agent that run a first-pass third-party security review, with a built-in skeptic.** Point it at a vendor's SOC 2 report, security questionnaire and policies, plus a short intake note about what the business wants to buy, and it produces a risk tier, a control-by-control assessment mapped to NIST CSF 2.0, NIST SP 800-53 Rev. 5 and ISO/IEC 27001:2022, findings with remediation deadlines, contradictions between what the vendor claims and what the evidence shows, follow-up questions, and a recommended outcome for a human risk owner to decide on.

> All sample vendors, people and documents in this repo are fictional.

## Why this exists

Vendor security reviews are slow, repetitive and important. Most of an analyst's time goes to reading: finding the audit period in a 90-page SOC 2 report, checking whether the product being bought is even in scope, and noticing that the questionnaire says "MFA everywhere" while the auditor found admin accounts without it. That reading is exactly what a language model is good at, as long as the method is explicit and the output is checked.

I've run third-party risk programs in regulated healthcare, and automating this first pass with Claude cut my assessment time by more than 80%. This repo is a public, from-scratch version of that approach: the method is written down as skills, the output is a fixed schema, and an eval checks that the agent catches what it should.

## How it works

```
 intake note ─┐      1. DRAFT                2. CHALLENGE              3. RESOLVE
 SOC 2 report ─┼─►  vendor-security-review ─► skeptic-review ─────►  reviewer accepts / rejects /
 questionnaire ┤     ├ soc2-report-reader     questions the intake,   marks "needs an answer" for
 policies/DPA ─┘     └ questionnaire-gap-check the vendor and the     every challenge ─► findings.json
                                               draft itself                             report.md
                                                                                        evals/score.py
```

1. **Tier first.** The vendor is tiered from the intake note (data, access, criticality) before any vendor evidence is read, so a polished trust center can't talk the tier down.
2. **Read the audit report.** The `soc2-report-reader` skill pulls out type, period, opinion, scope, exceptions, subservice organizations and the controls we must run ourselves (CUECs), and checks that the purchased product is in scope.
3. **Assess 12 control domains.** Each is marked met, partially met, not met or not evidenced, with a citation. A questionnaire answer is treated as a claim, not evidence. Domains are modeled on SIG Lite and the CSA CAIQ and mapped to NIST and ISO controls (`skills/vendor-security-review/references/control-catalog.md`).
4. **Cross-check claims.** The `questionnaire-gap-check` skill flags every claim the evidence contradicts.
5. **Decide.** Findings get a severity and due date from a written rubric; the outcome is approve, approve with conditions, escalate or reject, with a re-review date by tier.
6. **Challenge it.** A separate skeptic step, with its own instructions (`skills/skeptic-review/`), questions three parties: the **requesting team** (is the data really "de-identified"? is the tool really "not critical"?), the **vendor** (do the numbers add up? what backs the absolutes?), and the **draft review** itself (does the evidence say what the draft claims? is each severity justified, in either direction?).
7. **Resolve every challenge.** The reviewer must accept each challenge and change the review, reject it with a reason, or mark it "needs an answer" and turn it into a question for the vendor or the requesting team. The report includes the full challenge log, so a risk owner can see what was questioned and why it was decided the way it was.

The agent never contacts a vendor or approves anything; it writes a report for a person.

## What's in the repo

| Path | What it is |
|---|---|
| `skills/vendor-security-review/` | The main skill, with risk tiering, severity rubric, control catalog (NIST/ISO mapping) and report template |
| `skills/soc2-report-reader/` | Extracts what reviewers need from a SOC 2 report |
| `skills/questionnaire-gap-check/` | Finds contradictions between vendor claims and evidence |
| `skills/skeptic-review/` | The "naysayer": challenges the requesting team, the vendor and the draft review |
| `agent/` | Python runner: loads the skills, sends the vendor documents (Markdown, text or PDF) to Claude, enforces the output schema, writes `findings.json` and `report.md` |
| `samples/vendors/` | Two fictional vendors: **Brightpath Analytics** (healthcare analytics, nine planted issues) and **Ledgerly Payroll** (a well-run payroll vendor that should pass) |
| `evals/` | Answer keys for each sample vendor and a scorer that checks the agent's output against them |
| `examples/` | Real reports, final `findings.json` and the skeptic's `challenges.json` from the runs below |

## Quickstart

### Option 1: Claude Code (no API key needed)

The skills are linked into `.claude/skills/`, so Claude Code picks them up automatically.

```bash
git clone https://github.com/jasaan/claude-security-skills.git
cd claude-security-skills
claude
```

Then ask: *"Run a vendor security review on samples/vendors/brightpath-analytics."*

### Option 2: The agent (Claude API)

Requires Python 3.10+ and Claude API credentials (`ANTHROPIC_API_KEY`, or `ant auth login`). A review of a sample vendor makes four API calls and takes about 6 to 8 minutes.

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

python agent/review.py samples/vendors/brightpath-analytics
python agent/review.py samples/vendors/ledgerly-payroll
python evals/score.py --all
```

**Keep the API key out of files.** On macOS, store it in the keychain once and load it only for the command that needs it:

```bash
security add-generic-password -a "$USER" -s anthropic-api-key -w   # prompts; nothing echoed
ANTHROPIC_API_KEY="$(security find-generic-password -a "$USER" -s anthropic-api-key -w)" \
  python agent/review.py samples/vendors/brightpath-analytics
```

On Linux, `secret-tool` or `pass` do the same job. Never commit a key; `.env` and `*.key` are in `.gitignore`.

Reports land in `output/<vendor>/report.md`. To review a real vendor, make a folder with an `intake.md` and the vendor's documents (PDFs work) and point the agent at it. Use `--dry-run` to see what would be sent without calling the API.

## Results

Real runs on 2026-11-20 with Claude Opus 5.5 (high effort): four API calls per vendor, about 6 to 8 minutes each. Full output, including the skeptic's raw challenges, is in [`examples/`](examples/).

| Vendor | Tier | Outcome | Findings | Skeptic challenges | Eval |
|---|---|---|---|---|---|
| Brightpath Analytics | Tier 1 | Escalate | 1 critical, 7 high, 2 medium, 1 low | 10: 4 accepted, 1 rejected, 5 need an answer | **14/14** |
| Ledgerly Payroll | Tier 2 | Approve with conditions | 0 critical, 0 high, 3 medium, 6 low | 9: 2 accepted, 1 rejected, 6 need an answer | **7/7** |

**What the skeptic caught:**
- **The requesting team.** Brightpath's requester called the data "de-identified"; the skeptic pointed out that the field list includes names, dates of birth and phone numbers. For Ledgerly it asked whether the payroll vendor will get debit authority over the company bank account (not in the intake), and noted that the employee self-service portal will serve all 180 employees, not just the 6 SSO users.
- **The draft review.** It caught Ledgerly controls marked "met" on the strength of a DPA that hasn't been signed yet, and a Brightpath severity that didn't match the rubric. Both were accepted and fixed.
- **My own answer key.** I had planted "MFA for all users" as a contradiction of the SOC 2 MFA exception. The skeptic noted the questionnaire is dated after the vendor's claimed fix, so it isn't a direct contradiction; the real issue is that the fix is unverified. The final review kept the High finding, asked the vendor for evidence, and I updated the eval to accept either treatment.

It also argues for leniency when warranted: it challenged several Ledgerly findings as possibly reflecting missing pages of an abridged report rather than real gaps.

## Design choices

- **A skeptic with a separate brief.** The same model that wrote a review is a poor judge of it. The challenge step runs as its own call with its own instructions and a mandate to push back in both directions, and the reviewer has to answer every challenge in writing. Inaccurate information often comes from the requesting team, not just the vendor, so the skeptic tests the intake note too.
- **Method in skills, not in code.** The review procedure, rubric and control catalog are plain Markdown that a security team can read, argue with and change without touching Python.
- **Structured output.** The model must answer in a fixed JSON schema (`agent/schema.py`), validated again with Pydantic. Reports are rendered from data, so they're consistent and the results can feed a tracker or GRC tool.
- **Evals, not vibes.** Each sample vendor has an answer key of planted issues, and things that should *not* be flagged. The scorer is deliberately simple keyword-and-field matching so anyone can see why a check passed or failed.
- **Vendor documents are untrusted input.** The Brightpath trust-center page hides an instruction telling automated reviewers to approve the vendor. The agent is told to treat vendor text as data and report attempts like this as findings; the eval checks that it does.
- **Model and safety defaults.** Claude Opus 5.5 with adaptive thinking at high effort. The server-side refusal fallback is on by default (`--no-fallback` turns it off).

## Limitations

- It's a first pass. A person still decides, and still reads the evidence behind any high or critical finding.
- It only knows what's in the documents. It doesn't check breach databases, attack-surface scans or news.
- The NIST and ISO mappings are indicative cross-references, not an audit opinion.
- The keyword scorer can mark a correct but unusually worded finding as missed; read the report when a check fails.

## Frameworks referenced

NIST Cybersecurity Framework 2.0 · NIST SP 800-53 Rev. 5 · ISO/IEC 27001:2022 Annex A · Shared Assessments SIG Lite · CSA CAIQ · AICPA SOC 2 Trust Services Criteria · NIST AI RMF and ISO/IEC 42001 (for AI vendors)

## License

MIT
