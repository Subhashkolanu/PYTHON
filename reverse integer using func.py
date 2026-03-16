def rev_num(n=123):
    rev=0
    while n!=0:
        rem=n%10
        rev=rev*10+rem
        n=n//10
    return rev
n=int(input("Enter the number to reverse : "))
print("Reversed no : ",rev_num(n))
print("Default value : ",rev_num())