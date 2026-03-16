t1=input("str-1 : ")
t2=input("str-2 : ")
t1=t1.lower().replace(" ","")
t2=t2.lower().replace(" ","")
if sorted(t1)==sorted(t2):
    print("Anagram")
else:
    print("Not a Anagram")