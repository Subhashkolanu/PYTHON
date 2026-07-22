temp = int(input("Enter temperature : "))
unit = input("Enter unit (C/F) : ").upper()

if unit == "C":
    print(f"{temp}°C to {round((temp*9/5)+32,1)}°F")
elif unit == "F":
    print(f"{temp}°F to {round((temp-32)*5/9,1)}°C")