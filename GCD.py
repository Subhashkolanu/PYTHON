a=int(input("Enter a value : "))
b=int(input("Enter a value : "))
smaller=min(a,b)
for i in range (1,smaller+1):
    if a%i==0 and b%i==0:
        gcd=i
print("GCD {} ".format(gcd))