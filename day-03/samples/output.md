## Summary

Mobile checkout Pay tap does nothing for some customers since today's 2pm deploy; desktop reportedly fine.

## Severity

**P1** — payment path broken on mobile after a same-day deploy, finance is already asking, two concrete order ids attached.

## Expected vs Actual

- **Expected:** UNSET (report never stated what should happen beyond finishing payment)
- **Actual:** customers `"tap Pay and nothing happens"` on mobile

## Repro steps

1. On mobile, reach checkout and tap Pay
2. Observe: nothing happens (no further detail given)

## Environment

- Browser: Safari (one report); others UNSET
- OS / device: iPhone (one report); others UNSET
- App / site version: UNSET
- Account type: UNSET
- Deploy marker: `"2pm deploy"` today

## Impact

- Who: `"a few customers on mobile"`; exact count UNSET
- Orders named: `O-18421`, `O-18429`
- Desktop: `"desktop seems fine"`
- Stakeholders: finance is asking

## MISSING

- [ ] Exact error / network response when Pay is tapped (console, API status, blank spinner?)
- [ ] Browser + OS versions for `O-18421` and `O-18429` (and whether both were Safari/iPhone)
- [ ] Can CS reproduce on a test account right now?
- [ ] Which payment provider / method (card, Apple Pay, etc.)?
- [ ] How many total failed checkouts since the 2pm deploy (analytics or gateway)?
- [ ] Confirm deploy diff that touched checkout / pay

## Suggested next owner action

Payments eng: pull gateway + frontend logs for `O-18421` / `O-18429` around the 2pm deploy, and reply to Maya with the MISSING checklist.
