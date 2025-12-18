num = int(input("Enter the integer: "))
original_num = num
count = 0
temporary = original_num
sum = 0
while temporary>0:
    count+=1
    temporary//=10
sum = 0
while num > 0:
    digit = num%10
    sum+= digit**count
    num//=10
if original_num == sum:
   print(f"{original_num} is An Armstrong Number")
else:
    print(f"{original_num} is not an Armstrong Number")