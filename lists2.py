import random
list_a = []

for i in range(5):
    list_a.append(random.randrange(1, 10))

list_a.sort()

print(list_a)

list_a.reverse()

print(list_a)

list_a.insert(2, 3)

print(list_a)

list_a.remove(3)

print(list_a)

list_a.pop(4)

print(list_a)