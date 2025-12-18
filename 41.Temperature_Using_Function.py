def temperature():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
print("The temperature in Fahrenheit is:", temperature())   
