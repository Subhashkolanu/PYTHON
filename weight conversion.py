a = int(input('''choose the option :
               1. kilograms to pound
               2. Pound to kilograms'''))
if a == 1:
    kg=float(input("Enter the weight in kg : "))
    pound = kg*2.2
    print(pound)
else:
    pound=float(input("Enter the weight in pounds : "))
    kg = pound*0.45
    print(kg)