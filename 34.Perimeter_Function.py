def perimeter():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    peri = 2 * (length + width)
    return peri
print("The perimeter of the rectangle is:", perimeter())