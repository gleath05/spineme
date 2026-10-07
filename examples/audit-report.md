# Example: callback replay

This is a hypothetical teaching example, not a finding from a real repository.
Assume `callbacks.py:18–31` validates a callback and then calls `fulfill(order_id)`
each time, with no event-ID deduplication, atomic state transition, or downstream
idempotency. Replaying an accepted event therefore fulfills the order twice.

| Field | Example |
| --- | --- |
| Scope | Backend only |
| Readiness | NOT READY for the requested scope |
| Overall production readiness | NOT ASSESSED |
| Finding | PR-001 — Duplicate fulfillment on callback replay |
| Severity / confidence | HIGH / CONFIRMED by the hypothetical deterministic path |
| Blocker | YES — duplicate irreversible fulfillment |
| Evidence | Assumed callback implementation and downstream behavior above |
| Missing validation | No replay or concurrent-delivery test has been executed |

## Remediation handoff

Make processing of a repeated event idempotent, including concurrent delivery.
Choose a design appropriate to the real storage and fulfillment boundary. An
in-memory flag or non-atomic check-then-write is insufficient. Preserve legitimate
retries after failure and define recovery from a crash between persistence and
external fulfillment. Add targeted replay, concurrency, and partial-failure checks.

## Verification criteria

Inspect the actual fix and its complete side-effect boundary. A replay must not
repeat fulfillment; concurrent requests must not both win; crashes must remain
recoverable. Record which checks ran and which evidence is missing. Do not mark
RESOLVED solely because a uniqueness column was added or unrelated tests pass.
