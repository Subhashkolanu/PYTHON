n=int(input("Enter a three digit positive no :"))
m=n
print(m)
a=0
while n!=0:
    rem = n%10
    a = a+rem*rem*rem
    n = n/10
if int(a)==int(m):
    print("Armstrong Number")
else:
    print("Not a Armstrong number")