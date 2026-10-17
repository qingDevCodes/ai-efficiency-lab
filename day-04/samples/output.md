## Breaking changes

- The `/v2/invoices` API now uses `customer_id` instead of `client_id`. If you call this endpoint directly, rename the field in your requests and in any code that reads responses. (#418)

## New

- Send up to 50 invoices at once from the invoice list, drafts with no due date included. (#412, #421)
- Payment reminders can now be set per customer, so each customer can get reminders on their own days instead of one schedule for the whole account. (#424)

## Improved

- The invoice list loads 200 rows at a time instead of everything at once. (#429)

## Fixed

- Invoice PDFs now show the correct currency symbol for SEK and NOK instead of "?". (#415)
- Password reset links now stop working once they've been used. (#427)

## NEEDS A HUMAN

- #434 `fix: timezone`: which screen or feature was affected, and what did users see before the fix?
