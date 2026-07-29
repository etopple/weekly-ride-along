# Worked example — an issue built to spec

**This issue is invented.** The company, the customers, the incidents, and the
numbers are all fabricated to demonstrate the structure. Do not send it, and do
not copy its stories — the entire premise of the format is that the stories are
*yours* and *true*.

Written as if from the owner of a fictional 12-person IT services firm.

Read it for the **mechanics**: where the "I never realized" fact sits, how a
technical term gets glossed inline, how a vendor is omitted when the vendor is
the villain, how an unfinished fix gets hedged out loud, and where the
copy-pasteable line lands.

Annotations in `<!-- -->` are not part of the email.

---

**Subject:** Ride along with me — the invoice that changed one digit

Hi {{first_name}},

Thank you to everyone who replied to the last one. The consensus was that the story about what attackers do *before* they steal anything was the part worth your time, so this week leads with a cousin of it.

<!-- Opening acknowledges repliers by topic, never by name. Two sentences. -->

**1. The invoice that changed one digit**

Here's the part of a wire-fraud story nobody tells you: the fake invoice usually isn't fake. This month a construction client of ours — about 40 people — nearly paid a real invoice, from a real vendor they'd worked with for years, for real work that had actually been done. One thing had changed: the bank routing number. An attacker had been sitting quietly in the vendor's email for weeks, reading, learning the rhythm of who bills whom, and waiting. Then they intercepted a legitimate invoice on its way out, altered nine characters, and sent it along.

That's why the usual advice — *look for typos, check the sender address* — fails here. There were no typos. The sender address was correct, because it was the vendor's actual mailbox. Everything a careful person is trained to check was clean. What caught it was mundane: an accounting clerk who had a personal rule about calling to confirm any change in payment details, and who called a number from an old contract rather than the number printed on the new invoice. That last detail is the whole ballgame.

<!-- The "I never realized" fact: the invoice is genuine and the sender is
     real; only the routing number changed. Anonymized to vertical +
     headcount. The mechanism, not the moral, is the content. -->

**Try this (two minutes):** send one message to whoever pays your bills, saying: *"If any vendor's bank details ever change, call them to confirm — using a phone number from an older document, never the number on the new invoice."* That single sentence, made into a rule, is one of the highest-value controls a small business has, and it costs nothing. You can't verify a change using the same channel that delivered it.

<!-- Concrete action, doable today, by a non-technical reader. Lands on an
     aphorism. -->

**2. The report that used to take a Friday**

Every month our team spent most of a Friday assembling a status report: pulling numbers out of four systems, pasting them into a document, writing the same six paragraphs of explanation with different numbers in them. Nobody's favorite day.

This month I watched an AI do the assembly. It reads the four systems, builds the tables, drafts the explanation in our own house style — and then stops, and waits for a human to read every line before anything leaves the building. It's been running two cycles now and holding. I'm not calling it finished: the first cycle it confidently mislabeled one column, which is exactly why the human step isn't optional and never will be. What used to be most of a Friday is now about twenty minutes of reading and correcting.

<!-- The showcase is deliberately unglamorous, and admits a failure. The
     hedge — "two cycles and holding", "mislabeled a column" — is stated in
     public. That reads as credibility, and it's safe if it breaks later. -->

What this makes possible for a business like yours: any report your team rebuilds from the same sources every month is a candidate. The work isn't the typing, it's the assembling — and the assembling is what this is good at. The reading and the judgment stay with the person whose name goes on it.

**Try this (copy-paste):** take the most repetitive document your business produces and paste this into ChatGPT or Copilot along with two past examples: *"Here are two examples of a document we produce every month. Identify the parts that change, the parts that never change, and the source each changing part comes from. Then tell me what someone would have to give you each month to draft it."* The answer is a plain-English spec for automating it — and it's often shorter than people expect.

<!-- A literal clipboard-ready prompt, tied directly to the story above it. -->

**3. Why "we'll do it after the busy season" never happens**

A quick one. Talking to owners this month, I keep hearing the same sentence about improvement projects: *we'll get to it after the busy season.* I've said it myself. What I've noticed is that the businesses that actually change things don't wait for a quiet month — they pick something small enough to finish *during* a loud one. The report above wasn't a project. It was one annoyance, handled once, in a week that was otherwise full. **Try this:** name the one recurring annoyance you'd most like to never think about again. Not the biggest problem — the most repetitive one. That's the one to start with, and you can start it this week.

<!-- Shorter slot, ~1/3 the length. Framed by reader consequence, and it
     reaches back to segment 2 as its proof point. -->

Thanks for reading. Reply and tell me which of the three was worth your time — last issue's replies decided what you just read.

— [First name]

*P.S. Please feel free to forward this to anyone who'd get something out of it — it's meant to be shared.*

---

## What this example is demonstrating

| Move | Where |
|---|---|
| Acknowledge repliers by topic, not name | Opening line |
| "I never realized" fact | The invoice is real; only nine characters changed |
| Explain why the standard advice fails | Paragraph 2 of segment 1 |
| Anonymize to vertical + headcount | "a construction client — about 40 people" |
| Action a non-technical reader can take today | "call using a number from an older document" |
| Aphorism to close a segment | "You can't verify a change using the same channel that delivered it" |
| Showcase told for the mechanism, not the outcome | Segment 2, paragraph 2 |
| Admit a failure | "confidently mislabeled one column" |
| Hedge an unfinished result out loud | "two cycles now and holding… not calling it finished" |
| "What this makes possible" line | Segment 2, paragraph 3 |
| Literal copy-pasteable prompt | End of segment 2 |
| Segment 3 shorter, reader-framed, reaches back | Segment 3 |
| Closing question that produces replies | Sign-off |
| Forward P.S. | Last line |
| No pricing, no "book a call", anywhere | Whole issue |
