# Receive an uppercase string
# Transform it into an string of unicodes
# Transform it back into the string

norm_string = input("Enter a string to hide in uppercase: ")
secret_string = ""

for char in norm_string:
    secret_string += str(ord(char)-23)

print(secret_string)
norm_string = ""
for i in range(0, len(secret_string)-1, 2):
    char_code = secret_string[i] + secret_string[i+1]
    #print(int(char_code) + 23)
    #print(int(secret_string[i] + secret_string[i + 1]) + 23)
    norm_string += chr(int(char_code)+23)

print(norm_string)
print(ord(" "))
