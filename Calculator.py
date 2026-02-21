a = int(input("Enter the value of a :"))
b = int(input("Enter the value of b :"))
print("Choose your operation : +,-,*,/,//,**")
op = input("Enter your choice : ")
if op == "+":
    add = a+b
    print("Addition = ",add)
    
elif op == "-":
    subtraction = a-b
    print("subtraction = ",subtraction)
elif op == "*":
    multplication = a*b
    print("multiplication = ",multplication)
elif op == "/":
    if b!=0:
            real_division = a/b
            print("Real division = ",real_division)
    else:
        print("Division is not possible")
elif op == "//":
    if b!=0:
        floor_division = a//b
        print("Floor division = ",floor_division)
    else:
     print("Division is not possible")
elif op == "**":
    exponent  = a**b
    print("Exponent = ",exponent)
else:
    print("Invalid operation.")