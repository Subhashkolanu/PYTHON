percentage = int(input("Enter your percentage : "))
if percentage>70:
    print("GRADE A")
elif percentage>65 and percentage<70:
    print("GRADE B+")
elif percentage>60 and percentage<65:
    print("GRADE B")
elif percentage>55 and percentage<60:
    print("GRADE C")
else:
    print("Failed")