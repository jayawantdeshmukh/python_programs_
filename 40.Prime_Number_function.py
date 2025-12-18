def prime():
    num = int(input("Enter a number: "))
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if (num % i) == 0:
                return False
        return True
    else:
        return False

if prime():
    print("The number is a prime number.")
else:
    print("The number is not a prime number.")