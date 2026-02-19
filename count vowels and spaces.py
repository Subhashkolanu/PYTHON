a=input('Enter string : ')
a=a.lower()
v='aeiou'
vc=0
cc=0
for ch in a:
    if ch.isalpha():
        if ch in v:
            vc+=1
        else:
            cc+=1
print('Vowel count : ',vc)
print('Consonants count : ',cc)