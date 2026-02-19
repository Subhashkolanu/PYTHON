l=list(map(int,input().split()))
es=0
os=0
for i in l:
    if i %2 ==0:
        es+=i
    else:
        os+=i
print('Even sum : ',es)
print('Odd sum : ',os)