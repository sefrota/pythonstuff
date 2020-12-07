#Generate a list with 5 values between 1 and 9
import random

list_a = []

for i in range(5):
    list_a.append(random.randrange(1, 10))

print(list_a)
