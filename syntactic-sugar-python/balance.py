debit = 300.00
credit = 450.00

print(
    f"Debit: ${debit:.2f}, Credit: ${credit:.2f}, Balance: ${credit - debit:.2f}"
)

print(
    "Debit: ${:.2f}, Credit: ${:.2f}, Balance: ${:.2f}".format(
        debit, credit, credit - debit
    )
)
