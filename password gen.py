import random
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*"
password=""
all=letters+numbers+symbols
print("Enter the length of password (min : 8) : ")
size=int(input())
for i in range (size):
    password+=random.choice(all)
    if i == size-1:
        print('Suggested password : ',password)