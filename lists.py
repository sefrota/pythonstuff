rand_list = ["string", 1.234, 5]
one_to_ten = list(range(11))
rand_list = rand_list + one_to_ten
print(rand_list[0])
print(len(rand_list))
first_three = rand_list[0:3]

for i in first_three:
    print("{} : {}".format(first_three.index(i), i))

print(first_three[0] * 3)
print("string" in first_three)
print("Index of string : ", first_three.index("string"))
print("How many strings: ", first_three.count("string"))
first_three[0] = "New String"

for i in first_three:
    print("{} : {}".format(first_three.index(i), i))

first_three.append("Another")

