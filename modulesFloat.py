from decimal import Decimal as D

sum = D(0)
sum += D("0.01")
sum += D("0.01")
sum += D("0.01")
sum += D("0.01")
sum += D("0.01")
sum += D("0.01")
sum -= D("0.06")

print("Sum = ", sum)