a=("Enter your Integer: ")
original_a= a 
reversed_a= 0
while a>0:
    digit=a%10
    reversed_a=reversed_a*10+digit
    a//=10
if original_a==reversed_a:
    print(f"{original_a} is a palindrome")
else:
    print(f"{original_a} is not a palindrome")
