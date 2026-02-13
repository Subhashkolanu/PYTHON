text=input()
text=text.lower()
text=text.replace(" ","")
if text==text[::-1]:
    print('Palindrome')
else:
    print('Not a palindrome')