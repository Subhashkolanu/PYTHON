import random
lt=[]
for i in range(20):
    x=random.randint(1,100)
    lt.append(x)
print("Randome list:",lt)
avg=0
sum=0
for ele in lt:
    sum+=ele
avg=sum/len(lt)
print("Average value :",avg)
lt.sort()
print('Sorted list : ',lt)
print('Maximum :',lt[-1])
print('Minimum :',lt[0])
print('second maximum :',lt[-2])
print('second min : ',lt[1])
ec=0
for ele in lt:
    ele%2==0
    ec+=1
print('No of even numbers : ',ec)