from typing import LiteralString


def execute_sql(query: LiteralString):
    print(f"Pretending to execute: {query}")


# Valid examples
execute_sql("SELECT * FROM users")

table = "users"
execute_sql(f"SELECT * FROM {table}")

# Invalid: user input is not allowed
user_input = input("\nEnter table name: ")
execute_sql(f"SELECT * FROM {user_input}")
