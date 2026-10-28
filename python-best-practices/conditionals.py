# Avoid this:
# def shipping_cost(country, items):
#     if country is not None:
#         if country == "US":
#             if len(items) > 0:  # Non-empty cart?
#                 if len(items) > 10:  # Free shipping?
#                     return 0
#                 else:
#                     return 5
#             else:
#                 return 0
#         elif country == "CA":
#             if len(items) > 0:  # Non-empty cart?
#                 return 10
#             else:
#                 return 0
#         else:
#             # Other countries
#             if len(items) > 0:  # Non-empty cart?
#                 return 20
#             else:
#                 return 0
#     else:
#         raise ValueError("invalid country")


# Favor this:
def shipping_cost(country, items):
    if country is None:
        raise ValueError("invalid country")

    if not items:  # Empty cart?
        return 0

    if country == "US":
        return 0 if len(items) > 10 else 5

    if country == "CA":
        return 10

    return 20  # Other countries
