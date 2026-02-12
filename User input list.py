lt=input().split()
rlt=[ ]
for ele in lt:
    if ele not in rlt:
        rlt.append(ele)
        print(rlt)
print(type(rlt))