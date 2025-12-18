def year():
    yr = int(input("Enter a year: "))
    if (yr % 4 == 0 and yr % 100 != 0) or (yr % 400 == 0):
        return True
    else:
        return False
if year():
    print("The year is a leap year.")

else:
    print("The year is not a leap year.")
    