def sum_no(*t):
    s=0
    for ele in t:
        s=s+ele
    print(s)
    return
a=int(input("Enter num-1 : "))
b=int(input("Enter num-2 : "))
c=int(input("Enter num-3 : "))
d=int(input("Enter num-4 : "))
sum_no(a,b)
sum_no(a,b,c)
sum_no(a,b,c,d)