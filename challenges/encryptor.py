# 1. Receive a message and then encrypt it by shifting the characters by a requested amount to the right
# A becomes D, B becomes E for example. Also, decrypt the message back again

## A-Z have the numbers 65-90 in unicode
## a-z have the numbers 97-122 in unicode

orig_message = input("Enter your message to be encrypted and the encryption key integer: ")
key = input("How many characters should we shift (1-26)")

key = int(key)
encrypted_message = ""

for char in orig_message:
    char_unicode = ord(char)
    char_unicode += key

    if char.isalpha():
        if char.isupper():
            if char_unicode > ord('Z'):
                char_unicode -=26
            elif char_unicode < ord('A'):
                char_unicode +=26
        else:
            if char_unicode > ord('z'):
                char_unicode -=26
            elif char_unicode < ord('a'):
                char_unicode +=26
        encrypted_message += chr(char_unicode)
    else:
        encrypted_message += char

print(encrypted_message)

orig_message = ""

for char in encrypted_message:
    if char.isalpha():
        char_code = ord(char)
        char_code -= key
        if char.isupper():
            if char_code > ord('Z'):
                char_code -=26
            elif char_code < ord('A'):
                char_code += 26
        else:
            if char_code > ord('z'):
                char_code -=26
            elif char_code < ord('a'):
                char_code +=26
        orig_message += chr(char_code)
    else:
        orig_message += char

print(orig_message)