# Uncomment in Python 3.14+

# from string.templatelib import Interpolation

# name = "Pythonista"
# site = "realpython.com"
# template = t"Hello, {name}! Welcome to {site}!"


# def build_report(template):
#     parts = ["Account Report:\n"]
#     for item in template:
#         match item:
#             case str() as s:
#                 parts.append(s.strip(", ").upper())
#             case Interpolation() as i:
#                 parts.append(f"> ${i.value:{i.format_spec}}")
#         parts.append("\n")
#     return "".join(parts)


# report = build_report(template)
# print(report)
