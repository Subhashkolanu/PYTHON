name = input("Enter your name : ")
print("Hello, " + name + "! Welcome to VVITU")
int_marks = int(input("Enter your INTERMEDIATE marks : "))
jee_per = int(input("Enter your JEE percentile : "))
if int_marks >= 750 or jee_per >=80:
  print("YOU ARE ELIGIBLE FOR ADMISSION : ")
else:
    print("YOU ARE NOT ELIGIBLE FOR ADMISSION : ")
admission = input("Enter your choice Y/N : ")
if admission == "Y":
   print('''These are the courses offered here
        1.CSE
        2.ECE
        3.EEE
        4.ME
        5.CIVIL ENGINEERING''')
branch = input("Choose branch : ")

if branch == "CSE":
    print("YOU HAVE CHOSEN CSE")

elif branch == "ECE":
    print("YOU HAVE CHOSEN ECE")

elif branch == "EEE":
    print("YOU HAVE CHOSEN EEE")

elif branch == "ME":
    print("YOU HAVE CHOSEN MECHANICAL ENGINEERING")

elif branch == "CE":
    print("YOU HAVE CHOSEN CIVIL ENGINEERING")

else:
    print("INVALID BRANCH")
