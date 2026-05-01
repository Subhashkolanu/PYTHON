import random
a=int(input("Enter seed value: "))
random.seed(a)
lt=[]
for i in range(20):
    x=random.randint(1,100)
    lt.append(x)
print("Generated list :",lt)
s=0
slt=sum(lt)/len(lt)
print("Average:",slt)
print("Largest:",max((lt)))
print("Smallest:",min(lt))
lt.sort()
print("Second largest:",lt[-1])
print("Second smallest:",lt[1])
ec=0
for ele in lt:
    if ele%2==0:
        ec+=1
print("Sum of even numbers:",ec)