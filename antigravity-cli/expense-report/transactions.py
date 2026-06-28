"""Summarize a CSV of personal transactions by category."""

import csv


def report(path):
    rows = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)

    totals = {}
    count = 0
    grand_total = 0.0
    for row in rows:
        category = row["category"]
        amount = float(row["amount"])
        if category not in totals:
            totals[category] = 0.0
        totals[category] += amount
        grand_total += amount
        count += 1

    lines = []
    lines.append("Expense report")
    lines.append("=" * 32)
    for category in sorted(totals, key=lambda c: totals[c], reverse=True):
        share = totals[category] / grand_total * 100
        lines.append(f"{category:<14}{totals[category]:>10} ({share:.1f}%)")
    lines.append("-" * 32)
    lines.append(f"{'TOTAL':<14}{grand_total:>10}")
    lines.append(f"{count} transactions")
    return "\n".join(lines)
