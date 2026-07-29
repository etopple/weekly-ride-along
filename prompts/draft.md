# Prompt — Draft This Week's Issue

Run in an interactive session, after the author has picked ideas off the
harvest sheet. Output is a markdown draft with an internal header block.

---

## Before you write

1. Read the author's voice guide. Match the gear used for customers —
   warm and careful, not the internal or the promotional voice.
2. Read `reference/showcase-bank.md` for segment 2 material.
3. Read the **reader feedback log** at the bottom of this file. It overrides
   any general instinct about what belongs in the email.
4. Read the last issue. Note anything it promised to follow up on.

---

## Structure

Subject line: `Ride along with me — <the concrete thing>`. Concrete, not
clever. The reference implementation's best-performing subject was
*"the email wearing your name."*

Greeting: `Hi {{first_name}},`

**Opening (2 sentences max).** If the last issue produced replies, acknowledge
them by *topic*, never by name: *"A couple of you told me the inbox-rule story
was the eye-opener, so this week leans into that."* This rewards repliers,
trains the reply habit, and proves a human reads the inbox.

### Segment 1 — Security / risk (the lead)

Must contain one **"I never realized..." fact** — a concrete attacker or
defender mechanic the reader has never seen described. This is the bar. If
you can't clear it, tell the author rather than shipping a soft segment.

- **What happened** — one anonymized story from this week. Vertical +
  headcount only.
- **What it means** — name the real term, gloss it inline *immediately*,
  give the felt meaning. `DMARC (Domain-based Message Authentication,
  Reporting and Conformance — the acronym matters less than the job) is the
  public instruction that tells every mail server on earth...`
- **Try this (two minutes)** — a concrete action for today.

If the reader's own vendor (you) is implicated in the action you're
recommending, **say so first and invite the check anyway.** *"And if that's
us — ask anyway. It either means your domain is mid-tune, or you just did my
quality control for me. I'll take it."*

### Segment 2 — Capability showcase

Ride-along framing: *"this week I watched an AI do X."* Tell a real build
from your own shop.

- The story, told for the mechanism rather than the outcome. Notice how
  unglamorous the good ones are.
- One line of **"what this makes possible for a business like yours."**
- Optionally **"one thing we learned"** — a failure or near-miss. These are
  disproportionately trusted. *"An AI transcript confidently mis-heard the
  name of a company's core software — twice, two different ways."*
- **Try this (copy-paste)** — a literal prompt, search string, or command.
  Not advice. Something that goes on a clipboard.

**Not a pitch.** No pricing, no "book a call." The only door-opener permitted:
*"if this sparks an idea for your business, hit reply."*

### Segment 3 — Rotating slot

~1/3 shorter than the others. Frame by **reader consequence**, not by your
own industry's internal concerns. Ideal when it carries a through-line back
to segment 2 — the earlier story becomes the proof point for this one's
lesson.

### Close

*"Reply and tell me which of the three was worth your time — last week's
replies literally decided what you just read."*

Sign with first name only if your mail system appends a signature block.

`P.S. Please feel free to forward this to anyone who'd get something out of
it — it's meant to be shared.`

The P.S. is not decoration. In the reference implementation the first
attributed sales opportunity arrived, the day after issue 001, via a forward.

---

## Output: draft header block

Write the draft to `drafts/YYYY-MM-DD-issue-NNN.md`, opening with a blockquoted
header the reader never sees:

```
> **Draft header — not part of the email.**
> Structure: 1 <topic> / 2 <topic> / 3 <topic>
> Sources: <ticket IDs, log entries, calendar events>
>
> **Fact-check flags for the author:**
> 1. <claim> — <what you could and could not verify> — <keep / soften / cut?>
> 2. <anonymization decision> — <confirm?>
> 3. <vendor named or omitted> — <say the word if you want it named>
>
> **Per-recipient variants:** <any personalized postscript, and why>
```

Phrase every flag as a question the author can answer yes/no. This block is
the most valuable output of the whole job — it is where you say what you are
unsure about instead of guessing quietly.

---

## Hard rules

- **No fabrication.** Every incident, number, and claim traces to a source.
  Unverified detail gets softened or cut, and always flagged.
- **Hedge in public when you're hedging in private.** *"Deployed a few days
  now and holding — I'm not calling it done yet."* Reads as credibility, and
  it's safe if the problem recurs.
- **Anonymize to vertical + headcount.** Never a name, domain, or identifying
  detail. When the story is about an active deal, drop the vertical too.
- **Omit the vendor when the vendor is the villain.** Blame the mechanism.
- **Nothing sends until the author explicitly approves.**
- If the issue tells readers to run a check, **run that check across every
  recipient domain before sending** and report the results in the header.

---

## Reader feedback log

*Append to this after every issue. It is the living part of the recipe.*

**Issue 001** — 2 replies, both positive. Signal: **segment 1 > 2 > 3.**
The insider-mechanics reveal is the hook; the copy-paste line is the second
hook; the ops segment is respected but least loved.
> *"Most interesting — I never realized attackers would hide emails first."*
> *"I appreciate both 1 & 2 more, but see the value in 3."*

Adjustments adopted from issue 002 onward:
1. Security stays the lead; every security segment carries an "I never
   realized" fact.
2. Segment 2 always ships a literal copy-pasteable line, and its story
   showcases a real build.
3. Segment 3 runs ~1/3 shorter, framed by reader consequence. Do **not** cut
   it on n=2 replies — watch another cycle.
4. Keep the closing "which of the three" question. It is what produces replies.
5. Open the next issue by acknowledging replies.
