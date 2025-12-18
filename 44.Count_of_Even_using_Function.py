def even(list):
    count = 0
    for num in list:
        if num % 2 == 0:
            count += 1
    return count
n = int(input("Enter the number of elements in the list: "))
numbers = []
for i in range(n):
    element = int(input("Enter element: "))
    numbers.append(element)
print("The count of even numbers in the list is:", even(numbers))
