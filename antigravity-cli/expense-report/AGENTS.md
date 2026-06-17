# Project conventions

This is a small command-line tool that reads a CSV of personal transactions and
prints a per-category expense summary.

## Money

- Represent every monetary amount with `decimal.Decimal`, never `float`.
- Quantize money to exactly two decimal places before displaying it.

## Style

- Keep functions small and single-purpose.
- Standard library only. No third-party dependencies.
