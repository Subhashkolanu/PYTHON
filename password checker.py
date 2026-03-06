import string
dcp=input('Enter your password : ')
digit=False
p=string.punctuation
pun=False
upper=False
lower=False
if len(p)>=8:
    for char in p:
        if char.isupper():
            upper=True
        elif char.islower():
            lower=True
        elif char.isdigit():
            digit=True
        elif char in p:
            pun=True
else:
    print('Insufficient length')
if upper == True and lower == True and digit == True and pun == True and len(p)>=8:
    print('Strong password')
else:
    print('Weak password')