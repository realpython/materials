debit = 300.00
credit = 450.00

template = """
Account Report
Credit:  ${credit:.2f}
Debit:  -${debit:.2f}
________________
Balance: ${balance:.2f}"""

print(
    template.format(
        credit=credit,
        debit=debit,
        balance=credit - debit,
    )
)

template = """
Account Report
Credit:  $%(credit).2f
Debit:  -$%(debit).2f
________________
Balance: $%(balance).2f"""

print(
    template
    % {
        "credit": credit,
        "debit": debit,
        "balance": credit - debit,
    }
)
