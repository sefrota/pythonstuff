# print(type("3"))
# print(type('3'))
# print(type('''3'''))

samp_string = "This is a very important string"

print("Length: ", len(samp_string))
print(samp_string[0])
print(samp_string[-1])
print(samp_string[0:4]) #till 4th non inclusive
print(samp_string[8:])
print("Every other", samp_string[0:-1:2]) # Start from the beginning, until the end, stepping by 2 characters
print("Reverse", samp_string[::-1])
print("Green " + "Eggs")
print("Hello" * 5)
num_string = str(4)

for char in samp_string:
    print(char)

for i in range(0, len(samp_string)-1, 2):
    print(samp_string[i] + samp_string[i+1])

# A - Z : 65 - 90
# a - z : 97 - 122

print("A = ", ord("A"))
print("65 = ", chr(65))

