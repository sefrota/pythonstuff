def add_numbers(num_1, num_2):
    return num_1 + num_2


print("5 + 4 =", add_numbers(5, 4))


def change_name():
    global name
    name = "Jerry"


name = "Tom"
change_name()

print(name)


def is_float(str_val):
    try:
        float(str_val)
        return True
    except ValueError:
        return False


print("Is 'banana' a float?", is_float("banana"))
print("Is 2 a float?", is_float(2))