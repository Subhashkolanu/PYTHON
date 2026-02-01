n = int(input("Enter number : "))
s=0
m=n
while n!=0:
    rem = n%10
    s=s+rem
    n=n//10
print("sum of digits of",m,"is",s)