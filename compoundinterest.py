principle=int(input("Enter ammount : "))
time=int(input("Enter time in years : "))
rate=float(input("Enter interst (%) : "))
ammount = principle*(1+rate/100)**time
print("Ammount : ",int(ammount))
compund=ammount-principle
print("Compound : ",int(compund))
