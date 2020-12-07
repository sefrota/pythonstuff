rand_string = "      this is an important string     "
rand_string = rand_string.lstrip()
rand_string = rand_string.rstrip()
rand_string = rand_string.strip()

print(rand_string)

print(rand_string.capitalize())

print(rand_string.upper())
print(rand_string.lower())

a_list = ["Bunch", "of", "random", "words"]
print(" ".join(a_list))

a_list_2 = rand_string.split()

for i in a_list_2:
    print(i)

print("How many is :", rand_string.count("is"))
print("Where is :", rand_string.find("string"))
print("Where is :", rand_string.replace("string", "banana"))


letter_z = "z"

print("Is z a letter or a number: ", letter_z.isalnum())
print("Is z a letter : ", letter_z.isalpha())
print("Is z a number : ", letter_z.isdigit())
print("Is z a number : ", letter_z.islower())
print("Is z a number : ", letter_z.isupper())
print("Is z a number : ", letter_z.isspace())