a=input()
b={}
for ch in a:
    if ch in b:
        b[ch]+=1
    else:
        b[ch]=1
for x in b:
    print("{}: {}".format(x,b[x]))