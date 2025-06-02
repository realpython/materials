def to_string(template):
    def convert(value, conversion):
        func = {"a": ascii, "r": repr, "s": str}.get(conversion, lambda x: x)
        return func(value)

    parts = []
    for item in template:
        if isinstance(item, str):
            parts.append(item)
        else:
            value = format(convert(item.value, item.conversion), item.format_spec)
            parts.append(value)
    return "".join(parts)


price = 234.8765
print(to_string(t"The price is ${price:.2f}"))

header = "Report"
print(to_string(t"{header:=^20}"))
