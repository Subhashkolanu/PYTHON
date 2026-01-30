n=int(input("Enter a three digit positive no :"))
m=n
print(m)
a=0
while n!=0:
    rem = n%10
    a = a+rem**3
    n = n//10
if a==m:
    print("Armstrong Number")
else:
    print("Not a Armstrong number")
