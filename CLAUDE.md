# CLAUDE.md: Project Rulebook

This file sets the rules for this project. Claude reads it at the start of every session.
**If a request conflicts with these rules, stop and ask Rachel first.**

---

## 1. What this project is

An evergreen, "set-it-and-forget-it" lead generation system for **Rachel Gonsalves**, Licensed Life & Health
Insurance Advisor with **Experior Financial Group Inc.** (Simcoe County / GTA, Ontario).

It has two assets:
1. **The ADHD-Friendly Financial Planning Workbook**, a free, fillable, printable PDF lead magnet.
2. **A static landing page** where people get the workbook in exchange for their name and email. It then points
   them to (a) book a free, no-obligation **Experior Financial Analysis (EFA)** or (b) learn about a flexible
   career in financial services.

**Goal:** once it's live, nothing has to be done daily or weekly. The only ongoing "task" is replying when a
lead books a call.

The full checklist is in [PLAN.md](PLAN.md).

---

## 2. ADHD-first working rules (how Claude works with Rachel)

- **One thing at a time.** Work on one PLAN.md checkbox per step. Don't start the next one until the current
  one is done or Rachel says to move on.
- **Every checkbox fits in one sitting** (about 30 minutes or less of Rachel's time). If it's bigger, split it.
- **Nothing recurring.** Never design a step that needs daily, weekly or monthly manual action. If something
  has to repeat, automate it (GitHub Actions, Tally integrations) or drop it.
- **Short answers.** Plain English, short paragraphs, no jargon walls.
- **End every work session with "Your one next step:"**, one sentence naming exactly one thing for Rachel to do.
- **Tick the box.** When a PLAN.md item is done, change `[ ]` to `[x]` so progress is visible.
- **Ask before big changes** (new tools, new accounts, anything that costs money, anything public).

---

## 3. Keep it simple and modular

- **Tech stack, and nothing more:** plain HTML + CSS, Jinja2 templates, one Python build script (`build.py`),
  WeasyPrint for the PDF. No JavaScript frameworks, no npm packages, no database, no CMS.
- **One file per workbook module** (`workbook/modules/01-snapshot.html`, `02-debt.html`, ...). Fixing one module
  never touches the others.
- **One shared stylesheet** (`styles/brand.css`) used by both the PDF and the landing page.
- **All personal details live in ONE file: `config.yaml`.** That's name, phone, email, booking link, career link,
  colours and disclosure text. Templates read from it. Changing a link means editing one line.
- Every folder gets a two-line `README.md` explaining what's in it.

### Planned folder layout
```
lead-magnet/
├── CLAUDE.md          ← this rulebook
├── PLAN.md            ← the checklist
├── config.yaml        ← all personal details & links (edit here only)
├── build.py           ← builds the PDF + site
├── requirements.txt
├── styles/brand.css
├── workbook/          ← workbook templates (one per module)
├── site/              ← landing page, thank-you page, privacy page
├── assets/            ← fonts, icons, cover image
└── .github/workflows/build.yml  ← auto-builds & publishes on every push
```

---

## 4. Zero-cost hosting

- **Hosting:** GitHub Pages (free) at a subdomain such as `workbook.rachelgonsalves.com`.
  Vercel's free tier is the only approved backup.
- **Forms:** Tally.so free plan (unlimited submissions, consent checkbox, redirect after submit).
- **Builds:** GitHub Actions (free for public repos). The PDF is built in the cloud, so nothing extra needs
  installing on Rachel's Windows PC.
- **No paid tools, plugins, themes or subscriptions** without Rachel's explicit OK.
- **No tracking pixels or ad scripts.** Privacy-friendly free analytics (such as GoatCounter) only if Rachel asks.

---

## 5. Privacy & security (non-negotiable)

- The parent folder `B:\Business\` holds **confidential client files**. Claude must **never open, read, copy,
  quote or commit** anything from `Applications/`, `illustrations/` or `CE credits/`, and never use real client
  names or numbers as examples.
- Images from `B:\Business\images\` may be used **only** after Rachel picks the file, and only by copying it into
  `lead-magnet/assets/`.
- The GitHub repo is **public** (free GitHub Pages needs that), so it must contain marketing content only.
  The `.gitignore` is a safety net, not a substitute for care.
- **Leads stay in Tally.** Lead data never goes into this repo, a spreadsheet in this folder, or the code.
- **No secrets in code:** no passwords, API keys or tokens in any file.

---

## 6. Canadian insurance marketing compliance

Every page of the workbook and website must pass this list. Rachel's agency and province rules always win.
When unsure, flag it for Experior compliance review instead of guessing.

### Tone & claims
- **Educational, not advice.** Explain concepts. Never recommend a specific product, insurer or policy.
- **No guarantees or projections.** No "guaranteed returns", no rates of return, no "your money will grow to...",
  no cash-value or dividend projections.
- **Soft language for outcomes:** use "may", "can help", "consider", "some families find...". Never use "will".
- **Examples must be labelled** *"Illustrative example only. Your situation will be different."*
- **No fear-based or pressure language:** no "act now", "before it's too late", "limited time", or scare stats
  without a source.
- **No disparaging** other advisors, insurers, banks or product types.
- **Stats need a source:** any statistic must name its source and year, or be left out.

### Registered accounts & investments
- Explain RRSP, TFSA, RESP and FHSA **generically** (what they are, who they might fit, where to learn more,
  e.g. canada.ca).
- Don't pitch segregated funds, mutual funds or any securities product. Don't give tax advice; say
  "talk to a tax professional".
- Don't hard-code contribution limits that change every year. Link to canada.ca instead.

### Required disclosures (on the workbook's back page and the website footer)
- Rachel Gonsalves, Licensed Life & Health Insurance Advisor (Ontario)
- Experior Financial Group Inc.
- *"This workbook is for educational purposes only and is not financial, tax, legal or insurance advice.
  Insurance products are subject to eligibility and underwriting. Speak with a licensed professional about
  your situation."*
- The exact wording lives in `config.yaml → disclosure` so compliance edits happen in one place.

### Calls to action
- Clear and calm: **"Book your free, no-obligation Experior Financial Analysis (EFA)."**
- Say what the EFA is (a conversation about your goals), how long it takes, and that there is no cost and
  no pressure.

### Career / agency opportunity page
- **No income or earnings claims.** No "six figures", no "replace your salary", no income screenshots.
- **No hype:** no "be your own boss", "get rich", or "passive income".
- State plainly: **a provincial life insurance licence (LLQP) is required, results vary, and it takes work.**
- Describe it as flexible, independent, helping families, with training and mentorship available.

### Lead form (CASL + PIPEDA)
- **CASL:** an **unchecked** opt-in checkbox for future emails, e.g. *"Yes, send me occasional tips and updates
  from Rachel Gonsalves. I can unsubscribe anytime."* Downloading the workbook must work without ticking it.
- Collect the minimum: first name, email, province, and optionally what they're interested in.
- **PIPEDA privacy notice** linked under the form: what's collected, why, where it's stored (Tally), how to
  ask for deletion, and a contact email.
- Every follow-up email must include Rachel's name, contact info and an unsubscribe link.

### Approval
- **Before anything goes public, the final PDF and website go to Experior's compliance team for approval.**
  Record the approval date in PLAN.md.

---

## 7. Style guide (calm, simple, ADHD-friendly)

**Look:** mostly white pages. Mauve is the only accent colour, with a very light tint for boxes.
It must stay readable when printed in black and white.

| Token            | Value      | Use                                        |
|------------------|------------|--------------------------------------------|
| `--mauve`        | `#8B7394`  | headings, progress bars, buttons, accents  |
| `--mauve-dark`   | `#5E4A67`  | body headings, button hover (AA contrast)  |
| `--mauve-tint`   | `#F4EFF6`  | fill-in boxes, callouts                    |
| `--ink`          | `#2E2A30`  | body text                                  |
| `--line`         | `#D9D2DC`  | box borders, dividers                      |
| `--white`        | `#FFFFFF`  | page background                            |

**Fonts** (free Google Fonts, embedded in the PDF):
- Script (cover and module titles **only**): *Great Vibes* or similar, never for body text.
- Body and UI: *Atkinson Hyperlegible* (designed for readability) or *Nunito Sans*.

**Layout rules**
- Body text at least **14pt** in the PDF (16pt preferred), headings **24pt or larger**. Web body text at least 18px.
- **One idea per page.** Wide margins. Lots of white space.
- **Progress bar** at the top of each module's first page ("Module 2 of 5").
- **Micro-steps:** every task is a checkbox labelled with a timer, "⏱ 5 min".
- **Stop points:** "Done for today? That still counts." after every 2–3 micro-steps.
- **Fill-in boxes beat tables.** Round numbers are OK. No math that needs a calculator.
- Short sentences. Grade 6–8 reading level. Explain any jargon the first time it appears.
- Use icons and simple shapes, not stock photos (keeps the PDF small and printer-friendly).
- Mobile-first landing page. Buttons at least 48px tall. Meets WCAG AA colour contrast.

---

## 8. Definition of done

Something is "done" only when **all** of these are true:
- [ ] `build.py` (or the GitHub Action) runs with no errors.
- [ ] The PDF opens and **fields are typeable** in Adobe Acrobat Reader and Chrome, and prints cleanly in B&W.
- [ ] The landing page works on a phone, every link and button works, and the form redirects to the download.
- [ ] Every page passes the compliance list in section 6.
- [ ] The matching PLAN.md box is ticked `[x]`.
