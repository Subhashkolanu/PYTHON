greet = "PUSHPA" #positive indexing
print(greet[0])
print(greet[5])

name = "joshua"
print(name[0])
print(name[5])

n=(input('Enter a number = '))
print(n[0])
print(n[-1])

num=int(input('Enter number : '))
ld = num%10
while num>10:
    num=num//10
print("First digit : ",num)
print("Last digit : ",ld)