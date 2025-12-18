def largest_number():
    numbers = []
    for i in range(3):
        num = float(input(f"Enter number {i+1}: "))
        numbers.append(num)
    numbers.sort()
    return numbers[-2]  
print("The second largest number is:", largest_number())