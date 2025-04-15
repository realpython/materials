accepted_emails = {"Bob", "Diana", "Charlie"}
target_customers = {"Alice", "Bob", "Charlie", "Diana", "Jane"}
target_customers &= accepted_emails
print(target_customers)

# Or

target_customers = {"Alice", "Bob", "Charlie", "Diana", "Jane"}
target_customers.intersection_update(accepted_emails)
print(target_customers)
