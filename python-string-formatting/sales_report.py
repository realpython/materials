REPORT_TEMPLATE = """
Monthly Sales Report
--------------------
Report Date Range: {start_date} to {end_date}

Number of Transactions: {sep:.>20} {transactions:,}
Average Transaction Value: {sep:.>11} ${avg_transaction:,.2f}

Total Sales: {sep:.>23} ${total_sales:,.2f}
"""


def build_sales_report(sales_data, report_template=REPORT_TEMPLATE):
    total_sales = sum(sale["amount"] for sale in sales_data)
    transactions = len(sales_data)
    avg_transaction = total_sales / transactions

    report = report_template.format(
        sep=".",
        start_date=sales_data[0]["date"],
        end_date=sales_data[-1]["date"],
        total_sales=total_sales,
        transactions=transactions,
        avg_transaction=avg_transaction,
    )

    return report


sales_data = [
    {"date": "2024-04-01", "amount": 100},
    {"date": "2024-04-02", "amount": 200},
    {"date": "2024-04-03", "amount": 300},
    {"date": "2024-04-04", "amount": 400},
    {"date": "2024-04-05", "amount": 500},
]

print(build_sales_report(sales_data))
