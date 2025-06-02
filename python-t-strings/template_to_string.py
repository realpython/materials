def to_string(template):
    parts = []
    for part in template:
        if isinstance(part, str):
            parts.append(part)
        else:
            value = {
                "a": ascii,
                "r": repr,
                "s": str}.get(part.conversion, lambda _: part.conversion)(part.value)
            value = format(value, part.format_spec)
            parts.append(value)
    return "".join(parts)


price = 234.8765
print(to_string(t"The price is ${price:.2f}"))  # noqa
print(to_string(t"The price is ${price!s:.2f}"))  # noqa
