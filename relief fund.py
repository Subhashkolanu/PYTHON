damage=input("Enter type of damage F/P : ")
income=int(input("Enter annual income : "))
if damage=="F" and income<300000:
    print("Relief fund : 200000")
elif damage=="F" and income>300000:
    print("Relief fund : 100000")
elif damage=="P" and income<300000:
    print("Relief fund : 100000")
else:
    print("Relief fund : 50000")