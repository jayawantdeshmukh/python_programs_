def number():
    num = int(input("Enter a number: "))
    return num % 2 == 0
if number():
    print("The number is even.")
else:
    print("The number is odd.")
    