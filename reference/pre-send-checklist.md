# Pre-send checklist

Run top to bottom. Every item exists because skipping it cost something.

## Content

- [ ] Read every word of the draft. All of it. It will be forwarded to people
      you've never met.
- [ ] Segment 1 contains one **"I never realized"** fact — a concrete mechanic
      the reader has never seen described.
- [ ] Segment 2 ends in a **literal copy-pasteable** line, prompt, or command.
- [ ] Segment 3 is noticeably shorter and framed by reader consequence.
- [ ] Closing question present: *"which of the three was worth your time."*
- [ ] Forward-me P.S. present.
- [ ] Nothing in the email reads as a pitch. No pricing. No "book a call."

## Truth

- [ ] Every fact-check flag in the draft header is answered.
- [ ] Every claim traces to a ticket, log entry, or verified source.
- [ ] Anything unverified is hedged in the copy itself
      (*"holding so far"* beats *"fixed"*).
- [ ] No customer name, person name, domain, or identifying detail anywhere.
      Vertical + headcount only — and drop the vertical too when the story
      involves an active deal.
- [ ] No vendor named as the villain of a story.

## The instruction you're giving readers

**If the issue tells readers to go check something, check it yourself first —
across every recipient domain.**

- [ ] Ran the check the email recommends, for every domain on the list.
- [ ] Any gaps found on your own accounts are **fixed before send**, or
      disclosed to that specific recipient in a personalized postscript.
- [ ] Verified through an independent path. Local DNS resolvers, VPN clients,
      and secure-DNS agents lie — the reference implementation got false
      NXDOMAIN results from an intercepting client mid-verification. Re-check
      via DNS-over-HTTPS JSON (`cloudflare-dns.com` / `dns.google`) or an
      external lookup service.

## List

- [ ] Recipient list `status` is `approved`, not `awaiting review`.
- [ ] Exclusions applied — as a filter in the query, not from memory.
- [ ] Unsubscribes still marked after the last refresh.
- [ ] Scanned for wrong-contact-at-right-company. Especially if this issue's
      story came from one of these accounts.
- [ ] Per-recipient variants prepared and attached to the right addresses.

## Send

- [ ] Send yourself a proof copy first. Read it in a real mail client, on a
      phone.
- [ ] Individual sends. Never CC. Never BCC. Never a marketing platform.
- [ ] Greeting personalized; no `{{first_name}}` survives in the output.
- [ ] Throttled (~1 send / 2s).
- [ ] Send log written: issue number, date, subject, recipients, failures,
      variants.

## After

- [ ] Watch the inbox for replies for 48 hours. Answer every one personally.
- [ ] Log what each replier said they valued — into the recipe file, not a
      report. The recipe is the living document.
- [ ] Mark used showcase-bank entries with the issue number.
- [ ] Note the hook the next issue should open with.
