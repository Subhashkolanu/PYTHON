file=open("basic_details","r")
n=int(input("Enter value : "))
for i in range(n):
    print(file.readline(),end="")
file.close()