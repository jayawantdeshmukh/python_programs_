def prime_numbers_in_range():
    lower = int(input("Enter the lower number of the range: "))
    upper = int(input("Enter the upper number of the range: "))
    primes = []
    for num in range(lower, upper + 1):
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes
print("Prime numbers in the given range are:", prime_numbers_in_range())