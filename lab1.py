#Printing first and last digits
n=int(input("Enter number : "))
n=abs(n)
l=n%10
while n>10:
    n=n//10
print(n,l)