s1 = input("Enter the data in string 1 : ")
s2 = input("Enter the data in string 2 : ")
if len(s1)!=len(s2):
    print("Strings are not of same length")
else:
    for i in range (len(s1)):
        print(s1[i]+s2[i],end = "")