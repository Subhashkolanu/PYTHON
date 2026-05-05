def sum_of_numbers(num):
    s=0
    while num!=0:
        rem=num%10
        s+=rem
        num=num//10
    return s
n=int(input("Interger number : "))
print("SUM :",sum_of_numbers(n))