# Spec: inspection_status

Ticket: #2 – Determine STK/MTK inspection status for a device

## What it does
Returns the STK/MTK inspection status of one device: "ok", "due_soon" or "overdue".

## Out of scope
- Calculating due dates from inspection intervals
- Loading or cleaning device data
- Deciding which devices need STK/MTK at all
- The maintenance priority score and the weekly list

## Interface
inspection_status(due_date: date, as_of_date: date) -> str

Location: src/medfleet/deadlines.py

## Rules (prototype assumptions)
| Days until due (due_date - as_of_date) | Status |
|---|---|
| negative (-1 or less) | "overdue" |
| 0 to 14 | "due_soon" |
| more than 14 | "ok" |

An inspection due today (0 days) is "due_soon", not "overdue".

## Before and after
- Before: both inputs are date objects; the device requires an inspection.
- After: exactly one of the three statuses is returned; nothing else changes.

## Invariants
- The existing days_until_due function and its tests stay unchanged.

## What can go wrong
- A date given as text (e.g. "2026-10-10") or None -> TypeError, no status returned.

## Executable checks
Check 1 (normal path)
- Given an STK due on 2026-10-10 and a reference date of 2026-10-01
- When the inspection status is requested
- Then it returns "due_soon"

Check 2 (something goes wrong)
- Given the due date is the text "2026-10-10" instead of a date
- When the inspection status is requested
- Then a TypeError is raised