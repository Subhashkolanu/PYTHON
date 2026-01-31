a = int(input('choose the option :\n 1. kilograms to pound\n 2. Pound to kilograms\n'))
if a == 1:
    kg=float(input("Enter the weight in kg : "))
    pound = kg*2.2
    print(kg,"kg to",pound,"lb")
elif a==2:
    pound=float(input("Enter the weight in pounds : "))
    kg = pound*0.45
    print(pound,"lb","to",kg,"kg")
else:
    print("conversion not found!")