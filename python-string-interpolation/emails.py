import csv

template = """
Dear {customer},

Thank you for your recent purchase of {product}.

Remember, our support team is always here to assist you.

Best regards,
{employee}
"""


def display_emails(template, data_file):
    with open(data_file) as file:
        for customer in csv.DictReader(file):
            print(template.format(**customer))


display_emails(template, "sales.csv")
