from string.templatelib import Interpolation

name = "Pythonista"
site = "realpython.com"
template = t"Hello, {name}! Welcome to {site}!"

# for item in template:
#     print(item)

# for s in template.strings:
#     print(s)

for value in template.values:
    print(value)

debit = 300.4344
credit = 450.5676
balance = credit - debit
template = t"Credit: {credit:.2f}, Debit: {debit:.2f}, Balance: {balance:.2f}"


# def build_report(template):
#     parts = ["Account Report:\n"]
#     for item in template:
#         if isinstance(item, str):
#             parts.append(item.strip(", ").upper())
#         else:
#             parts.append(f"> ${item.value:{item.format_spec}}")
#         parts.append("\n")
#     return "".join(parts)


def build_report(template):
    parts = ["Account Report:\n"]
    for item in template:
        match item:
            case str() as s:
                parts.append(s.strip(", ").upper())
            case Interpolation() as i:
                parts.append(f"> ${i.value:{i.format_spec}}")
        parts.append("\n")
    return "".join(parts)


report = build_report(template)
print(report)
