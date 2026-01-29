a = int(input("Enter the value of First integer : "))
b = int(input("Enter the value of Second integer : "))
if a>=b:
    if a>b:
        print(a,"is greater than",b)
    else:
        print(a,"is equal to ",b)
else:
    print(b,"is greater than ",a)