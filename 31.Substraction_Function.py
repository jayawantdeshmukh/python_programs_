def sub(num1, num2):
  
  sub_result = num1 - num2
  return sub_result


number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

result = sub(number1, number2)

print(f"The substraction of {number1} and {number2} is: {result}")
