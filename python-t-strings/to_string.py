from string.templatelib import Template


def to_string(template):
    if not isinstance(template, Template):
        raise TypeError("t-string expected")

    def convert(value, conversion):
        func = {"a": ascii, "r": repr, "s": str}.get(conversion, lambda x: x)
        return func(value)

    parts = []
    for item in template:
        if isinstance(item, str):
            parts.append(item)
        else:
            value = format(
                convert(item.value, item.conversion), item.format_spec
            )
            parts.append(value)
    return "".join(parts)


# Uncomment in Python 3.14+
# price = 234.8765
# print(to_string(t"The price is ${price:.2f}"))
#
# header = "Report"
# print(to_string(t"{header:=^20}"))
