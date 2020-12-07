import random

list_a = []

for i in range(5):
    list_a.append(random.randrange(1, 10))

i = len(list_a) - 1

while i > 0:
    j = 0
    while j < i:
        print("\nIs {} > {}".format(list_a[j], list_a[j+1]))
        print()
        if list_a[j] > list_a[j+1]:
            print("Switch")
            temp_item = list_a[j]
            list_a[j] = list_a[j + 1]
            list_a[j + 1] = temp_item
        j += 1
    i -= 1

print(list_a)