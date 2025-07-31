from decimal import Decimal, localcontext

with localcontext(prec=42):
    print(Decimal("1") / Decimal("42"))


print(Decimal("1") / Decimal("42"))
