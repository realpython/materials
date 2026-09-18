from handlers import register

@register("csv")
def emit(rows):
    return ",".join(str(row) for row in rows)
