# If age 5 "Go to Kindergarten"
# Ages from 6 to 17 goes to grades 1 through 12 "Go to grade 6"
# If age is greater than 17 then say "Go to college"

age = int(input("Input your age: "))

if age < 5:
    print("You're too young to school")
elif age == 5:
    print("Go to Kindergarten")
elif (5 < age) and (age < 18):
    print("Go to grade {}".format(age - 5))
else:
    print("Go to college")
