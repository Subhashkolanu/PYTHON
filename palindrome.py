n = int(input("Enter number : "))
rev=0
m=n
while n!=0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
if rev == m:
    print("Palindrome")
else:
    print("Not a palindrome")