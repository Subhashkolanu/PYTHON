age=int(input("Enter your age : "))
salary=float(input("Enter your salary : "))
cibil=int(input("Enter cibil score : "))

if age>21:
    if salary>30000:
        if cibil>=750:
            print("Loan approved!")
        else:
            print("Low cibil score")
    else:
        print("Salary not sufficient")
else:
    print("Age not eligile")