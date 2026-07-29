# The Weekly Ride-Along

**A recipe for a weekly customer email that people actually reply to — drafted by an AI that read your real week, approved by a human before it sends.**

Most B2B newsletters fail the same way: they're written *at* customers, from marketing's imagination, about nothing that happened. This recipe inverts that. Every issue is synthesized from your company's actual week — the tickets, the incidents, the projects, the meeting notes — and told in first person, as if the reader spent the week riding along with the owner.

Three segments. Each one ends in something the reader can do in about two minutes.

It works because it is the one email in their inbox that could only have come from you.

---

## Why this shape works

The recipe came out of a live run at [eTop Technology](https://etoptechnology.com), a ~30-client IT services firm, sent personally by the owner. What the first two issues showed:

- **The forward is the growth mechanism.** The first attributed sales opportunity arrived the day after issue 001, from a recipient forwarding it to someone else. A newsletter about *your actual week* is forwardable in a way that a newsletter about *industry trends* is not.
- **Replies are the tuning signal.** Unprompted replies to issue 001 rewrote the recipe for issue 002 — segment order, segment length, and the bar for what counts as an interesting fact all changed based on two emails.
- **It costs about half an hour a week** with an AI agent doing the harvest and the first draft, including the approval read.
- **Almost nobody unsubscribes** from an email that is a person talking about their week.

You don't need those numbers to be true for you. You need the structure, and the discipline in the rules section.

---

## The shape of one issue

```
Subject: Ride along with me — <the concrete thing>

Hi {{first_name}},

[Optional: acknowledge last issue's repliers by topic, never by name]

1. <RISK / INSIDER MECHANICS>   ← the lead. Must contain one "I never
   realized..." fact.
   What happened (anonymized) → what it means (name the term, gloss it
   inline) → Try this (2 minutes)

2. <CAPABILITY SHOWCASE>        ← a real build from your own shop, ride-along
   style.
   Story → "what this makes possible for a business like yours" →
   Try this (a literal copy-pasteable line or prompt)

3. <ROTATING SLOT>              ← ~1/3 shorter. Framed by reader consequence.

Reply and tell me which of the three was worth your time.

— <Your first name>

P.S. Please feel free to forward this to anyone who'd get something out of
it — it's meant to be shared.
```

A full worked example — invented, but built to spec — is in [`examples/worked-example.md`](examples/worked-example.md), annotated with why each move is there.

---

## The rules that make it work

These are not style preferences. Each one exists because skipping it cost something.

1. **Segment 1 leads, and it must contain one "I never realized" fact.** The hook is insider mechanics — a concrete thing that happens in your field that a normal business owner has never seen described. Not "phishing is on the rise." Not "supply chains are tightening." The bar was set by a reader who wrote back: *"I never realized attackers would hide emails first."* If your lead segment doesn't clear that bar, rewrite it or don't send.

2. **The capability segment ships a literal copy-pasteable line.** Not advice — a prompt, a search string, a checklist item. Something the reader can put on their clipboard. If the story itself gives them nothing to run, the segment still ends with something that does.

3. **Anonymize to vertical + headcount. Always.** "A law office, ~30 people." Never a customer name, a person's name, a domain, or a detail that identifies. This is what makes the stories tellable at all, and it is what earns you the right to keep telling them. When the story involves an active deal, drop the vertical too.

4. **No fabrication. Ever.** Every incident, number, and claim traces to a ticket, a log entry, or a source you can point at. If a detail is unverified — "no money moved," "the fix is holding" — soften it or cut it. Hedging in public reads as credibility: *"I'd rather tell you 'holding so far' than claim victory early."*

5. **Never a pitch.** No pricing, no "book a call." The only door-opener allowed is *"if this sparks an idea for your business, hit reply."* The showcase segment generates demand precisely because it refuses to sell.

6. **Individual sends, from a human mailbox.** Never CC, never BCC, never a marketing platform. Personalized greeting. The reply-to is a person who reads replies. This is the entire premise — a broadcast tool breaks it.

7. **A human approves every issue before it sends.** The agent drafts. A person reads every word. Non-negotiable.

8. **Ask the closing question.** *"Reply and tell me which of the three was worth your time."* This is what produces the replies, and the replies are what tune the next issue. Then open the next issue by acknowledging them — it rewards repliers, trains the habit, and proves a human is on the other end.

9. **Warm list only.** Customers and prospects you've actually met, quoted, or have an open deal with. Personal sends from your own mailbox to a cold list is a deliverability and CAN-SPAM problem. Cold outreach is a different machine; don't run it through this one.

---

## The weekly loop

```
  Harvest ──▶ Draft ──▶ Fact-check ──▶ Approve ──▶ Send ──▶ Log replies
   (agent)   (agent)     (agent)       (human)    (script)    (human)
      ▲                                                          │
      └──────────────── feeds next week's recipe ────────────────┘
```

### 1. Harvest (agent, automated)

Pull the last 7 days from wherever your work actually leaves a trace:

- **Your ticketing / job / case system** — security or safety incidents, anything a monitor caught before a human did, any theme appearing 3+ times, saves and wins.
- **Your own project log or notes** — what you built or learned this week that a reader could copy a piece of.
- **Your calendar** — site visits, conferences, customer meetings that produced an observation.
- **A curated showcase bank** — see below.

Prompt: [`prompts/harvest.md`](prompts/harvest.md)

Automate this part. Run it as a scheduled, **read-only** agent early in the week that emails *the author only* an idea sheet — not a draft, an idea sheet. The author picks two or three ideas; drafting happens in a session where a human can push back.

### 2. Draft (agent, in session)

Feed the harvest plus your voice guide to the drafting prompt. It produces a markdown draft opening with a **header block the reader never sees**:

- sources used (ticket IDs, log entries — internal only)
- **fact-check flags** — anything the agent could not verify, each phrased as a question answerable yes/no

Prompt: [`prompts/draft.md`](prompts/draft.md)

That header block is the highest-leverage part of the whole system. It is where the agent tells you what it is unsure about instead of quietly guessing.

### 3. Fact-check (agent, then human)

If the issue tells readers to go look at something — run this lookup, check this setting, pull this report — **check it yourself first, across every recipient, before you send.**

In the live run, one issue told readers to run a public lookup on their own domain. The pre-send sweep found that three of the author's *own customers* would have failed that lookup. They were fixed the same night, before the email went out. Had it shipped unchecked, the email would have invited 65 people to discover the author's own gap.

Where a gap can't be closed in time, **say so, to that specific recipient, in a personalized postscript.** Volunteered transparency reads as trustworthy; being caught reads as sloppy.

### 4. Approve (human)

Read every word. Answer the fact-check flags. Cut anything you'd be uncomfortable seeing forwarded to someone you've never met — because it will be.

### 5. Send (script)

One message per recipient, individually, from a real mailbox, throttled. Log every send.

Script: [`scripts/send.py`](scripts/send.py) — dry-run by default; mail backend is a stub you implement (Microsoft Graph, Gmail API, or authenticated SMTP).

### 6. Log replies

Every reply is signal. Write down what each reader said they valued, and **fold it into the recipe file itself** — not into a report nobody rereads. The recipe is a living document.

---

## The showcase bank

Segment 2 needs a real build or win to showcase every single week, and some weeks your week is boring. So keep a bank.

A curated file of pre-anonymized, customer-safe descriptions of real things you've built or shipped. Each entry:

- **Real thing** — one paragraph, plain language, no product names, no customer names.
- **What's possible line** — one sentence generalizing it to the reader's business.
- **used:** — mark with the issue number when it runs, so entries rotate.

Template + samples: [`reference/showcase-bank.md`](reference/showcase-bank.md)

Add an entry every time something ships. Then the segment writes itself on the weeks you have nothing.

---

## The recipient list

Two segments, one email:

- **Customers** — decision-maker contacts at your active accounts.
- **Warm prospects only** — people you've met, quoted, or have an open opportunity with.

Cache the list; refresh monthly, not per send. Have a human eyeball it before the first send and after every refresh — in the live run the list contained the *wrong contact at the right company*, and that week's lead story was the other person's incident.

Schema: [`reference/recipients.schema.json`](reference/recipients.schema.json)

**Encode exclusions as data, not memory.** Any brand, business line, or segment that shouldn't receive this edition goes in the query — not in your head, and not in the head of whoever runs it next. Same for any bulk-imported list from years ago: mark it excluded permanently.

---

## Voice

Write a voice guide for yourself before issue 001 and hand it to the agent every time. Yours shouldn't be a copy of anyone else's. Some portable principles:

- **First person, always.** "I watched an AI do X this week." Never "our team is pleased to announce."
- **Written-you is tighter than spoken-you.** Keep the arc — extend the idea, give the example, land the aphorism — and cut the verbal filler.
- **One dry aside per segment, maximum.**
- **Name the real term, then gloss it inline immediately.** Readers are not stupid; they're just not in your field.
- **No competitor or vendor bashing.** When a vendor's product is the villain of the story, omit the brand and blame the mechanism.
- **Land on an aphorism when one fits.** *"You can't protect what you can't see." "Boring is a feature." "Not impressive — useful."*

The fastest way to build the guide: paste 5–10 things you've already written — emails, posts, a long Slack message — into an AI and ask it to describe your patterns, then edit what it gets wrong. Keep it to two pages.

---

## Adapting it to your field

The three-segment structure generalizes; the topics don't. Swap segment 1 for whatever risk your customers carry and you see the inside of:

| Your business | Segment 1 (the lead) | Segment 2 (capability) |
|---|---|---|
| IT / managed services | Security mechanics | An AI build from your shop |
| Accounting | Audit and compliance traps | Automation you run internally |
| Law | The clause that bit someone | How you're using AI on documents |
| Insurance | The claim that got denied, and why | Underwriting / ops tooling |
| Construction / trades | The inspection failure | Estimating / scheduling tooling |
| Healthcare admin | The denied reimbursement pattern | Intake or coding automation |
| Logistics | The shipment that vanished | Tracking / exception tooling |

The invariant: **you see something your customers cannot see, and it costs you nothing to show them.**

---

## Repo contents

```
prompts/harvest.md               weekly harvest → idea sheet
prompts/draft.md                 idea sheet + voice guide → draft w/ fact-check header
reference/showcase-bank.md       template + sample entries
reference/recipients.schema.json warm-list schema, approval gate, unsubscribe rules
reference/pre-send-checklist.md  content / truth / list / send / after
examples/worked-example.md       an invented issue, annotated
scripts/send.py                  individual throttled sends + send log
```

## Start here

1. Write your voice guide (two pages, from your own past writing).
2. Build the recipient list. Warm only. Have a human approve it.
3. Seed the showcase bank with 3–5 real things you've built or fixed.
4. Run the harvest prompt by hand once, to see what your week actually contains.
5. Draft issue 001. Read every word. Send it to yourself first.
6. Send it. Then answer every reply personally, and write down what they said.

Step 6 is the whole thing. The recipe in this repo is mostly a record of what readers said, turned into rules.

---

## Credits

Developed and run at [eTop Technology](https://etoptechnology.com) by BJ Pote, built with [Claude Code](https://claude.com/claude-code). Shared because the structure is more useful than it is proprietary.

Everything here is the method, not the material: no customer names, no client stories, no recipient data. The worked example is invented. Bring your own week — that's the entire point of the format.

MIT licensed. Take it, fork it, make it yours. If you run it, the interesting thing to report back is what your readers reply to — that's the part no template can give you.
