lt=input().split()
rlt=[]
for ele in lt:
    if ele not in rlt:
        rlt.append(ele)
for i in range(len(rlt)):
    rlt[i]=int(rlt[i])
print(rlt)