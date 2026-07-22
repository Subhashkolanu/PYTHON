weight = float(input('Enter your weight : '))
unit = input("Kilograms or pounds (K or L) : ").upper()
if unit == "K":
    print(f"{weight} kg converted to {round(weight*2.205,2)} lbs")
elif unit=="L":
    print(f"{weight} pounds converted to {round(weight/2.205,2)} kg's")
else:
    print("conversion not found!")