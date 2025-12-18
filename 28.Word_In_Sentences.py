input_string = input("Enter a string: ")

word_count = 0
in_word = False

for char in input_string:
    if char == ' ' or char == '\t' or char == '\n':
        in_word = False
    elif not in_word:
        word_count += 1
        in_word = True

print("Total number of words:", word_count)