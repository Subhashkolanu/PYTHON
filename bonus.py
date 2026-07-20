experience=int(input("Enter experience : "))
salary=int(input("Enter your salary : "))
if experience>=5:
    if salary<50000:
        b=salary*0.20
        salary+=b
        print("BONUS : ",b)
        print("Salary : ",salary)
    else:
        b=salary*0.10
        salary+=b
        print("BONUS : ",b)
        print("Salary : ",salary)
else:
    print("No bonus")
        
