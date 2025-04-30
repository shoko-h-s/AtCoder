from decimal import Decimal, ROUND_HALF_UP

x = float(input())

print(Decimal(str(x)).quantize(Decimal("1"), rounding=ROUND_HALF_UP))
