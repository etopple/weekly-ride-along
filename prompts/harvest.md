# Prompt — Weekly Harvest → Idea Sheet

Run this on a schedule (e.g. Wednesday early morning) as a **read-only** agent.
Its output is an idea sheet emailed to the author only — **never a draft, and
never anything that sends to readers.**

Replace the bracketed source calls with your own systems.

---

## Task

You are harvesting raw material for this week's Ride-Along email. You are not
writing the email. You are handing the author a menu.

### 1. Work system — last 7 days

[Query your ticketing/work system for the last 7 days, primary service board.]

If the result set is large, save the tool output to a file and extract
`[id, company, status, summary]` with `jq` rather than reading it inline —
full ticket bodies will blow your context for no benefit.

Scan for, in priority order:

- **Security incidents** — phishing reported, credential theft, identity alerts,
  business email compromise, anything where an attacker did something a normal
  person has never seen described.
- **Monitoring-generated tickets** — something that alerted before a human
  noticed. These are the best "invisible work" stories.
- **Patterns** — any theme appearing 3+ times across different customers.
  A pattern is inherently more interesting than an anecdote.
- **Saves and wins** — where the outcome was materially better because of
  something you do.

### 2. Your own work log — last 7 days

[Read the top of your project/daily log — the last ~100 lines.]

Looking for: what you built or learned with AI this week that a reader could
copy a *piece* of. Bias toward the unglamorous. "We used AI to generate the
diagnostic commands and ran them in the background so nobody got pulled off
their machine" beats any grand claim.

### 3. Calendar — last 7 days

[Query the author's calendar for the past week.]

Looking for: conferences, site visits, customer meetings that produced an
observation. Segment 3 material lives here.

### 4. Showcase bank

Read `reference/showcase-bank.md`. List entries with no `used:` marker.
Flag any entry that matches something that actually moved this week — those
are strongest, because they're current *and* pre-anonymized.

### 5. External filler — only if the week is thin

One industry item from the past 7 days, verified at harvest time with a source
link. **Never the lead.** If the week has real material, skip this entirely.

---

## Output format

Email the author only. Keep it scannable — this is a menu, not prose.

```
RIDE-ALONG IDEA SHEET — week of <dates>

SEGMENT 1 CANDIDATES (security / risk — needs an "I never realized" fact)
  A. <one line> — source: ticket #NNNN, <vertical>, ~N people
     The "never realized" fact: <the specific mechanic>
  B. ...

SEGMENT 2 CANDIDATES (capability showcase + copy-paste line)
  A. <one line> — source: log entry <date> / showcase bank #N
     Copy-paste line candidate: <the literal thing the reader would run>
  B. ...

SEGMENT 3 CANDIDATES (rotating, shorter)
  A. <one line> — source: <calendar event / observation>

UNUSED SHOWCASE BANK ENTRIES: #N, #N, #N

CARRIED FROM LAST ISSUE: <any hook the last issue promised to follow up on>

FLAGS
  - <anything that would need verification before it could be published>
  - <anything that can't be anonymized safely>
```

---

## Hard rules for this job

- **Read-only.** This job changes nothing and sends nothing to readers.
- **Exclusions are queries, not memory.** Any brand, business line, or customer
  segment that must not appear gets filtered in the query itself.
- **No fabrication.** Every candidate carries its source ID. A candidate you
  can't cite is not a candidate.
- **Anonymize at harvest time**, not at draft time — vertical + headcount only.
  Then the draft can never accidentally carry a name it never received.
- If the week produced nothing that clears the "I never realized" bar for
  segment 1, **say so explicitly at the top.** A thin week is information;
  a padded issue is a cost.
