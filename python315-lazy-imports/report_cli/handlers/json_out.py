from handlers import register

@register("json")
def emit(rows):
    return "[" + ", ".join(f'"{row}"' for row in rows) + "]"
