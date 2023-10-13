import psycopg2

# This code doesn't run because of the missing `psycopg2` library
# and the assumption of a certain database structure and setup.
# It's a demonstrative code only.

connection = psycopg2.connect(database="db", user="user", password="password")
cursor = connection.cursor()

role = "admin"

query_modulo = "SELECT * FROM users WHERE role = '%s'" % role
query_format = "SELECT * FROM users WHERE role = '{role}'".format(role=role)
query_f_string = f"SELECT * FROM users WHERE role = '{role}'"

cursor.execute(query_modulo)
cursor.execute(query_format)
cursor.execute(query_f_string)

# Correct query
query_template = "SELECT * FROM users WHERE role = %s"

cursor.execute(query_template, (role,))
