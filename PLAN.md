# PLAN.md: Evergreen Lead-Gen System

> **How to use this file:** do the **first unticked box**, then stop. Each box is one sitting or less.
> Boxes marked 🤖 are Claude's job. Boxes marked 🙋 need Rachel (a click, a login or a decision).
> Rules live in [CLAUDE.md](CLAUDE.md).

**Progress:** Phase 0 ✅ · Phase 1 ☐ · Phase 2 ☐ · Phase 3 ☐

---

## Decisions already made ✅

| Topic            | Decision                                                                    |
|------------------|-----------------------------------------------------------------------------|
| Look             | Calm and simple: white pages, mauve `#8B7394` accent, light tint boxes, prints well in B&W |
| EFA booking link | `https://rachelgonsalves.com` (one line in `config.yaml`; swap for Calendly or Google later if wanted) |
| Hosting          | GitHub Pages (free) at a subdomain, e.g. `workbook.rachelgonsalves.com`      |
| Form tool        | Tally.so (free)                                                             |
| PDF tool         | HTML/CSS + Jinja2 + WeasyPrint (fillable fields), built by GitHub Actions   |
| Province         | Ontario                                                                     |

---

## Phase 0: Setup (about one sitting)

- [x] 🤖 Create `config.yaml` with Rachel's name, licence line, Experior name, phone, email, website,
      `booking_url`, `career_url`, colours and disclosure text
- [x] 🤖 Create the folder skeleton (`styles/`, `workbook/`, `site/`, `assets/`) and `requirements.txt`
- [x] 🤖 `git init` this folder (**only** `lead-magnet/`, never `B:\Business`), first commit
- [ ] 🙋 Replace the `career_url` placeholder in `config.yaml` with your career info-call link (whenever you have it)
- [x] 🙋 Create a GitHub repo, e.g. `workbook` (public, needed for free Pages). Claude can do it with the
      GitHub CLI once Rachel says OK. → https://github.com/rachelgonsalves/workbook (draft site: https://rachelgonsalves.github.io/workbook/)
- [x] 🤖 Add `.github/workflows/build.yml`: on every push → install WeasyPrint → run `build.py` →
      publish `site/` + the PDF to GitHub Pages
- [x] 🙋 Turn on GitHub Pages (Settings → Pages → Source: **GitHub Actions**)

---

## Phase 1: ADHD-Friendly Financial Planning Workbook (PDF)

**Working title:** *"Money Made Manageable: A No-Shame, 5-Minutes-at-a-Time Family Money Workbook"*
(final title to be confirmed)

### 1A. Design system (build once, reuse everywhere)
- [x] 🤖 `styles/workbook.css`: colour tokens, embedded fonts, Letter page size, wide margins, 16pt body, 28pt headings
- [x] 🤖 Reusable pieces: **progress bar** ("Module 2 of 5"), **micro-step checkbox** ("⏱ 5 min"),
      **fill-in box**, **callout box**, **"Done for today? That still counts."** stop point,
      **page footer** with the short disclaimer and page number, plus a **module overview** page listing each module's 5-minute steps
- [x] 🤖 Make inputs fillable: text boxes, number boxes and checkboxes become real PDF form fields
      (WeasyPrint `pdf_forms`)
- [x] 🤖 Build a sample PDF to test the look (cover + Module 1 overview + Step 1 "Money in")
- [x] 🙋 Rachel approves the look before the full build (approved 2026-11-18)

### 1B. Front matter
- [x] 🤖 **Cover:** title, subtitle, "by Rachel Gonsalves", a simple mauve shape (no photo needed)
- [x] 🤖 **"How to use this workbook":** any order, 5 minutes at a time, round numbers are fine, no judgement
- [x] 🤖 **Your progress map:** 5 modules × checkboxes on one page, to tick and see progress

### 1C. Module 1: The "No-Shame" Money Snapshot
- [x] 🤖 Intro page: "This isn't a test. Messy numbers count."
- [x] 🤖 ⏱ **Money in:** monthly take-home pay boxes (you, partner, other income). Round numbers OK.
- [x] 🤖 ⏱ **Money owed:** simple list of name / balance / monthly payment. No interest math.
- [x] 🤖 ⏱ **What protection do I already have?** Checklist covering work group benefits, personal life
      insurance, mortgage insurance, critical illness, disability, and "not sure"
- [x] 🤖 ⏱ **My 3 numbers that matter:** money in, monthly debt payments, what's left. One summary box.

### 1D. Module 2: The Debt & Mortgage Accelerator
- [x] 🤖 ⏱ **Debt thermometers:** colour-in bars, one per debt, to see progress at a glance
- [x] 🤖 ⏱ **Snowball vs. avalanche in 2 pictures:** smallest balance first vs. highest interest first,
      with "pick the one you'll actually stick with"
- [x] 🤖 ⏱ **Freed-up cash tracker:** when one debt is gone, its payment rolls to the next (fill-in chain)
- [x] 🤖 ⏱ **Mortgage basics:** prepayment options to ask your lender about, renewal-date reminder, and
      questions to ask at renewal. Clearly *illustrative*, no rate promises.

### 1E. Module 3: Family Protection & Income Replacement Checklist
- [x] 🤖 ⏱ **Who depends on my income?** Simple "people map" fill-in
- [x] 🤖 ⏱ **Term vs. Permanent life insurance:** plain-English side-by-side ("renting vs. owning"
      analogy), no product names, no projections
- [x] 🤖 ⏱ **Critical Illness insurance in one page:** what it is, what it can help with, questions to ask
- [x] 🤖 ⏱ **Disability insurance in one page:** "your paycheque is your biggest asset" framing, plus
      group vs. personal coverage
- [x] 🤖 ⏱ **"Do I have enough?" check:** yes / no / not sure checkboxes, with no formula and every
      "not sure" pointing to the EFA

### 1F. Module 4: The "Future You" Emergency & Legacy Setup
- [x] 🤖 ⏱ **Emergency fund ladder:** step 1 starter cushion → step 2 one month → step 3 three to six
      months (fill-in goal boxes)
- [x] 🤖 ⏱ **TFSA / RRSP / RESP / FHSA in one line each,** plus "this might fit if…", with a link to
      canada.ca for current limits (no hard-coded numbers)
- [x] 🤖 ⏱ **Beneficiary checkup:** table of account/policy / who's named / last checked / ✓ up to date
- [x] 🤖 ⏱ **Will & Power of Attorney reminder:** short checklist (have one? where is it? who knows?)

### 1G. Module 5: Your Next Step
- [x] 🤖 **"What a free EFA looks like":** about 30–60 min, no cost, no pressure, what to bring
      (this workbook!), what you get
- [x] 🤖 **Book button** → `booking_url` from `config.yaml`, with the link written out for paper
      (QR codes skipped by Rachel's choice, 2026-11-18)
- [x] 🤖 **Back page, "Curious about a flexible career helping families?"** Work-from-home, independent,
      training available. **LLQP licence required, results vary, no income claims.** Link →
      `career_url`.
- [x] 🤖 **About Rachel + full disclosure + disclaimer** (from `config.yaml`)

### 1H. Build & test
- [x] 🤖 `build.py` renders all modules in order into one HTML file → WeasyPrint → `ADHD-Money-Workbook.pdf`
- [x] 🤖 GitHub Action builds the PDF automatically on every push
- [x] 🙋 Test: open in **Adobe Acrobat Reader** and **Chrome**, type in a few boxes, tick a few checkboxes,
      save, reopen, print one page in black and white (passed 2026-11-18)
- [x] 🤖 Run the compliance list (CLAUDE.md section 6) page by page and fix anything flagged
      (done 2026-11-18: 8 wording fixes. Questions to raise with Experior compliance are listed
      under Phase 3.)
- [ ] 🙋 Rachel reads it once and marks any wording changes

---

## Phase 2: Simple Static Landing Page

- [x] 🙋 Create a free Tally.so account (Claude gives exact click-by-click steps) → done 2026-11-19, form https://tally.so/r/ArpX10
- [ ] 🙋 Build the Tally form with these fields:
      name · email · **phone (required: Rachel's choice 2026-11-19, for higher-intent leads)** ·
      province (dropdown) · "What are you most interested in?"
      (Just the workbook / A free EFA / Learning about a career) · **unchecked** CASL opt-in checkbox ·
      link to privacy notice
- [ ] 🙋 Tally settings: **redirect on completion** → `https://workbook.rachelgonsalves.com/thank-you.html`,
      and turn on **email notification to Rachel** for each submission
- [ ] 🤖 `site/index.html`: headline ("Money stuff, 5 minutes at a time"), 3 benefit bullets,
      workbook cover image, embedded Tally form, short "About Rachel", disclosure footer
- [ ] 🤖 `site/thank-you.html`: big **Download your workbook** button, **Book your free EFA** button,
      and a smaller "Curious about a career?" link
- [ ] 🤖 `site/privacy.html`: PIPEDA privacy notice (what, why, where stored, how to delete, contact).
      Must say why the **phone number** is collected and that Rachel may call about the person's request
- [ ] 🤖 Social share image (Open Graph), favicon, page titles and descriptions
- [ ] 🤖 Mobile check, link check, colour-contrast check

### Custom subdomain (one-time, about 10 minutes)
- [ ] 🙋 At your domain registrar (where RachelGonsalves.com is managed), add **one DNS record**:
      ```
      Type:  CNAME
      Host:  workbook
      Value: rachelgonsalves.github.io
      ```
- [ ] 🙋 GitHub → Settings → Pages → Custom domain → `workbook.rachelgonsalves.com` → tick **Enforce HTTPS**
      (may take up to 24h to turn on)

---

## Phase 3: Launch & forget

- [ ] 🙋 Send the PDF and landing page link to **Experior compliance** for approval
      Worth asking them about specifically:
      · Career page (p. 28): is "independent work" and "flexible hours, often from home" OK, and do
        they need any extra recruiting wording?
      · Term vs. permanent, critical illness and disability descriptions (pp. 16–18)
      · EFA description (p. 26): "about 30 to 60 minutes, by phone or video"
      · Bio on the About page (p. 29)
      · Sign-up form: a **required phone number**, and follow-up calls to people who downloaded the
        workbook (Do Not Call List and CASL rules for calls and texts)
      · Sign-up form interest options "How to save on Income Tax / Business Tax" and
        "Savings and Investments": OK for a Life & Health advisor to offer?
      → Approved on: `____-__-__`
- [ ] 🤖 Apply any compliance edits → push (the site rebuilds itself)
- [ ] 🙋 **End-to-end test on your phone:** fill in the form → land on thank-you → download PDF →
      check the notification email arrived
- [ ] 🙋 Add the link to RachelGonsalves.com, Instagram/Facebook/LinkedIn bios, email signature,
      and business card QR code
- [ ] 🎉 Done. The only ongoing task is replying to people who book.

### Optional later (only if wanted, set up once)
- [ ] Tally → Google Sheets integration (free) so leads also land in a spreadsheet automatically
- [ ] Free MailerLite welcome email (one email, sent automatically) for people who ticked the opt-in
- [ ] Swap `booking_url` for a direct Calendly or Google booking page (one-line change in `config.yaml`)
