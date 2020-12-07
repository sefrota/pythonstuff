num_1, operator, num_2 = input("Input your calculation :").split()
result = "The result is {}"

num_1 = int(num_1)
num_2 = int(num_2)

if operator == "+":
    print(result.format(num_1 + num_2))
elif operator == "-":
    print(result.format(num_1 - num_2))
elif operator == "*":
    print(result.format(num_1 * num_2))
elif operator == "/":
    print(result.format(num_1 / num_2))
elif operator == "%":
    print(result.format(num_1 % num_2))
else:
    print("Wrong operator chosen")
