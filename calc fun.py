def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b if b != 0 else "Can't divide by zero"

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("1.Add  2.Sub  3.Mul  4.Div")
choice = int(input("Choose: "))

if choice == 1:
    print("Answer:", add(x, y))
elif choice == 2:
    print("Answer:", sub(x, y))
elif choice == 3:
    print("Answer:", mul(x, y))
elif choice == 4:
    print("Answer:", div(x, y))
else:
    print("Wrong choice")