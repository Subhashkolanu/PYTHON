def sod(n):
    s=0
    while n!=0:
        rem=n%10
        s=s+rem
        n=n//10
    print(s)
n=int(input())
sod(n)