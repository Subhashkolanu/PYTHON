a=input()
b=input()
if len(a)==len(b):
    c=""
    for i in range(len(a)):
        c+=b[i]+a[i]
    print("Combined string:",c)
else:
    print("Different length")