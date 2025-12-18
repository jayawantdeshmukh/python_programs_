def sum():
    result = 0 
    for i in range(1, n + 1):
        result += i
    return result
n = int(input("Enter a positive integer: "))
print("The sum of numbers from 1 to n: ",sum())