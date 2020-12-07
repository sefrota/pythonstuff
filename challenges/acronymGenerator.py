#Random Access Memory
#RAM

input_string = input("Enter your string to be acronymized: ")

a_list = input_string.split()

for i in a_list:
    print(i.capitalize()[0], end="")