from decimal import *

sum = Decimal(0)
sum += Decimal("0.011111111111111111111111")
sum += Decimal("0.011111111111111111111111")

print("Sum = ", sum)

sum -= Decimal("0.022222222222222222222222")

print("Sum = ", sum)
