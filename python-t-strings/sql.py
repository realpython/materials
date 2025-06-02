def sanitized_sql(template):
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


template = t"SELECT * FROM students WHERE name = '{username}';"
query, params = sanitized_sql(template)
print("Sanitized SQL Query:", query)
print("Parameters:", params)
