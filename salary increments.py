basic = int(input("Enter Basic salary : "))
da = int(input("Enter DA : "))
hra = int(input("Enter HRA:"))
da = basic*da/100
hra =basic*hra/100
print("Gross salary after increments = ",basic+hra+da)
