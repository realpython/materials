from string.templatelib import Template


def sanitized_sql(template):
    if not isinstance(template, Template):
        raise TypeError("t-string expected")
    parts = []
    params = []

    for item in template:
        if isinstance(item, str):
            parts.append(item)
        else:
            parts.append("?")
            params.append(item.value)

    query = "".join(parts)
    return query, tuple(params)


# Uncomment in Python 3.14+
# username = "'; DROP TABLE students;--"
# template = t"SELECT * FROM students WHERE name = {username}"
# query, params = sanitized_sql(template)
#
# print("Sanitized SQL Query:", query)
# print("Parameters:", params)
