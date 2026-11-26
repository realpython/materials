# 1. Use a layered architecture with enforced import direction

Date: 2026-10-26

## Status

Accepted

## Context

Contributors, human and automated, kept importing database code from the
domain layer. Reviews caught it late, and each fix touched several modules.

## Decision

Code lives in three layers: `orders.adapters`, `orders.services`, and
`orders.domain`. A layer may import only from layers below it. The rule is
enforced by an import-linter `layers` contract that runs in CI.

## Consequences

- Domain code can be tested without a database.
- New integrations go in `adapters`, so they can't leak into business rules.
- A cross-layer shortcut now fails CI instead of waiting for review.
