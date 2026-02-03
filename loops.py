for row in range(1,6):
    for col in range(row):
        print("VVITU", end=" ")
    print()
print("New")
n = 4
for i in range(1,n+1):
    for j in range(i):
        print("VVITU",end = " ")
    print()
print("New")
n = 5
for i in range(n,0,-1):
    for j in range(i):
        print("VVITU",end = " ")
    print()
print("New")
n = 3
for i in range(1,n+1):
    for j in range(i):
        print("*",end = " ")
    print()
print("New")
n = 4
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end = " ")
    print()
    print("New")
n = 4
for i in range(1,n+1):
    for j in range(1,i+1):
        print("",end = " ")
    print()
print("New")
word = "VVITU"
for i in range(1,len(word)+1):
    for j in range(i):
        print(word[j],end = " ")