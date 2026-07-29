#!/usr/bin/env python3
"""
Ride-Along sender — individual, personalized, throttled sends from a human
mailbox, with a send log.

Deliberately not a marketing platform. The whole premise of this email is that
it came from a person's mailbox and a person reads the replies. One message per
recipient. No CC. No BCC. No tracking pixels.

Usage:
    python send.py --issue 003 \\
                   --html drafts/2026-07-29-issue-003.html \\
                   --subject "Ride along with me — <thing>" \\
                   --recipients reference/recipients.json \\
                   --proof you@yourcompany.com          # send yourself one, then stop
    python send.py ... --send                            # the real thing

Nothing sends without --send. --proof implies a single send to that address.
"""

import argparse
import json
import os
import re
import sys
import time
from datetime import date
from pathlib import Path

THROTTLE_SECONDS = 2.0


# --------------------------------------------------------------------------
# Backend — implement send() for your mail system.
#
# The reference implementation calls its own MCP tool that sends as the author
# from their real mailbox. Pick whichever of these is true for you; all three
# preserve the "from a human's mailbox" property. A marketing platform does not.
# --------------------------------------------------------------------------

def send(to_addr: str, subject: str, html_body: str) -> None:
    """Send one message. Raise on failure."""
    raise NotImplementedError(
        "Wire up your mail backend. Options:\n"
        "  • Microsoft Graph  POST /me/sendMail  (delegated Mail.Send)\n"
        "  • Gmail API        users.messages.send\n"
        "  • Authenticated SMTP relay for your own domain\n"
        "Do NOT use unauthenticated relay or a marketing platform — the point "
        "is that this comes from a person."
    )


# --------------------------------------------------------------------------

def load_recipients(path: Path, include_prospects: bool = True) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))

    if data.get("status") != "approved":
        sys.exit(
            f"Recipient list status is {data.get('status')!r}, not 'approved'. "
            "A human reviews the list before it can be sent to."
        )

    people = list(data.get("clients", []))
    if include_prospects:
        people += list(data.get("prospects", []))

    out, seen = [], set()
    for p in people:
        email = (p.get("email") or "").strip()
        if not email:
            continue
        if p.get("unsubscribed"):
            continue
        key = email.lower()
        if key in seen:                      # same person, two companies
            continue
        seen.add(key)
        p = dict(p)
        p["first_name"] = p.get("first_name") or (p.get("name") or "").split()[0]
        out.append(p)
    return out


def personalize(html: str, person: dict, variants: dict[str, str]) -> str:
    body = html.replace("{{first_name}}", person["first_name"])
    extra = variants.get(person["email"].lower())
    if extra:
        # Per-recipient postscript, appended after the shared P.S.
        body = body.replace("</body>", f"<p><em>{extra}</em></p></body>") \
               if "</body>" in body else body + f"\n<p><em>{extra}</em></p>"
    return body


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--issue", required=True)
    ap.add_argument("--html", required=True, type=Path)
    ap.add_argument("--subject", required=True)
    ap.add_argument("--recipients", required=True, type=Path)
    ap.add_argument("--variants", type=Path,
                    help='JSON: {"someone@example.com": "per-recipient P.S.S. text"}')
    ap.add_argument("--clients-only", action="store_true")
    ap.add_argument("--proof", help="Send a single proof copy here, then exit.")
    ap.add_argument("--send", action="store_true", help="Actually send. Off by default.")
    args = ap.parse_args()

    html = args.html.read_text(encoding="utf-8")
    variants = json.loads(args.variants.read_text(encoding="utf-8")) if args.variants else {}
    variants = {k.lower(): v for k, v in variants.items()}

    if args.proof:
        proof = {"email": args.proof, "name": "Proof Copy", "first_name": "there",
                 "company": "(proof)"}
        if not args.send:
            sys.exit("Proof requires --send. Nothing sent.")
        send(args.proof, args.subject, personalize(html, proof, {}))
        print(f"Proof copy sent to {args.proof}. Read it on a phone before the real run.")
        return

    people = load_recipients(args.recipients, include_prospects=not args.clients_only)

    print(f"Issue {args.issue}: {len(people)} recipients, "
          f"{len(variants)} per-recipient variant(s).")
    if not args.send:
        for p in people:
            flag = "  [variant]" if p["email"].lower() in variants else ""
            print(f"  {p['first_name']:<12} {p['email']:<40} {p['company']}{flag}")
        print("\nDry run. Re-run with --send to send.")
        return

    sent, failures = [], []
    for i, p in enumerate(people, 1):
        try:
            send(p["email"], args.subject, personalize(html, p, variants))
            sent.append(p["email"])
            print(f"  [{i}/{len(people)}] sent  {p['email']}")
        except Exception as exc:                        # keep going; log the failure
            failures.append({"email": p["email"], "error": str(exc)})
            print(f"  [{i}/{len(people)}] FAIL  {p['email']}: {exc}", file=sys.stderr)
        time.sleep(THROTTLE_SECONDS)

    log_dir = Path("sent")
    log_dir.mkdir(exist_ok=True)
    log_path = log_dir / f"{date.today().isoformat()}-issue-{args.issue}.json"
    log_path.write_text(json.dumps({
        "issue": args.issue,
        "sent_date": date.today().isoformat(),
        "subject": args.subject,
        "html": str(args.html),
        "method": "individual sends from author mailbox; no CC/BCC",
        "total_sent": len(sent),
        "failures": len(failures),
        "variants": {k: v for k, v in variants.items()},
        "recipients": sent,
        "failed": failures,
    }, indent=2), encoding="utf-8")

    print(f"\n{len(sent)} sent, {len(failures)} failed. Log: {log_path}")
    print("Now watch the inbox for 48 hours and answer every reply personally.")


if __name__ == "__main__":
    main()
