temp = float(input("Enter the temperature value: "))
unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ")
if unit == 'F':
    F = (temp * 9/5) + 32
    print("Temperature in Fahrenheit:", F)
elif unit == 'C':
    C = (temp - 32) / 1.8
    print("Temperature in Celsius:", C)
else:
    print("Invalid unit! Please enter C or F.")
