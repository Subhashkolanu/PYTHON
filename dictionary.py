s=input('Enter a string : ')
print("captial=small? (Y/n) :")
c=input()
if c=='Y' or c=='y':
    s=s.lower()
d={}
for ch in s:
    if ch in d:
        d[ch]+=1
    else:
        d[ch]=1
print(d)
