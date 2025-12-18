input_string = "Hello World 123!"
uppercase_string = ""
for char in input_string:
    if 'a' <= char <= 'z':
        uppercase_string += chr(ord(char) - 32)
    else:
        uppercase_string += char

print("Original string:", input_string)
print("Uppercase string:", uppercase_string)

lowercase_string = ""
for char in input_string:
    if 'A' <= char <= 'Z':
               lowercase_string += chr(ord(char) + 32)
    else:
        lowercase_string += char

print("Lowercase string:", lowercase_string)