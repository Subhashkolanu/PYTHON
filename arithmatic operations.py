a = int(input("Enter the value of a :"))
b = int(input("Enter the value of b :"))
add = a+b
subtraction = a-b
multplication = a*b
if b!=0:
    real_division = a/b
    floor_division = a//b
exponent  = a**b
print("Choose your operation : +,-,*,/,//,**")
op = input("Enter your choice : ")
if op == "+":
    print("Addition = ",add)
elif op == "-":
    print("subtraction = ",subtraction)
elif op == "*":
    print("multiplication = ",multplication)
elif op == "/":
    if b!=0:
        print("Real division = ",real_division)
    else:
        print("Division is not possible")
elif op == "//":
    if b!=0:
        print("Floor division = ",floor_division)
    else:
     print("Division is not possible")
elif op == "**":
    print("Exponent = ",exponent)
else:
    print("Invalid operation.")