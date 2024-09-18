debit = 300
credit = 450

print(
    f"Debit: ${debit:.2f}, Credit: ${credit:.2f}, Balance: ${credit - debit:.2f}"
)

print(
    "Debit: ${:.2f}, Credit: ${:.2f}, Balance: ${:.2f}".format(
        debit, credit, credit - debit
    )
)

print(
    "Debit: $"
    + format(debit, ".2f")
    + ", Credit: $"
    + format(credit, ".2f")
    + ", Balance: $"
    + format(credit - debit, ".2f")
)
