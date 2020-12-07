# 1 - 18 - Important
# 21, 50, > 65 - Important
# Others not important

age = int(input("Enter age: "))

if (age >= 1) and (age <= 18):
    print("Important birthday")
elif (age == 21) or (age == 50):
    print("Important birthday")
elif not age < 65:
    print("Important birthday")
else:
    print("Sorry, not important birthday")
