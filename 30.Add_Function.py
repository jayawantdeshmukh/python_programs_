def add(num1, num2):
  
  sum_result = num1 + num2
  return sum_result


number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

result = add(number1, number2)

print(f"The sum of {number1} and {number2} is: {result}")

