name = input("Enter your name : ")
print("Hello", name, "! Welcome to VVITU")

int_marks = int(input("Enter your INTERMEDIATE marks : "))
jee_per = int(input("Enter your JEE percentile : "))

# checking eligibility
if int_marks >= 750 or jee_per >= 80:
    print("YOU ARE ELIGIBLE FOR ADMISSION :)")
    admission = "Y"
else:
    print("YOU ARE NOT ELIGIBLE FOR ADMISSION :(")
    admission = input("Enter your choice Y/N : ").upper()

if admission == "Y":
    print("\nThese are the courses offered here")
    print("1. CSE")
    print("2. ECE")
    print("3. EEE")
    print("4. ME")
    print("5. CE")

    branch = input("\nChoose branch : ").upper()

    if branch == "CSE":
        print("\nYOU HAVE CHOSEN CSE")
        print("Specialisations available:")
        print("1. AI-ML")
        print("2. AI-DS")
        print("3. CYBER SECURITY")

        spec = input("Choose your specialisation : ").upper()

        if spec == "AI-ML":
            print("\nSeat has been allotted in CSE-AI-ML")
            print("Fee per year = ₹130000")

        elif spec == "AI-DS":
            print("\nSeat has been allotted in CSE-AI-DS")
            print("Fee per year = ₹128000")

        elif spec == "CYBER SECURITY":
            print("\nSeat has been allotted in CSE-CYBER SECURITY")
            print("Fee per year = ₹135000")

        else:
            print("INVALID SPECIALISATION")

    elif branch == "ECE":
        print("\nYOU HAVE CHOSEN ECE")
        print("Fee per year = ₹100000")

    elif branch == "EEE":
        print("\nYOU HAVE CHOSEN EEE")
        print("Fee per year = ₹95000")

    elif branch == "ME":
        print("\nYOU HAVE CHOSEN MECHANICAL ENGINEERING")
        print("Fee per year = ₹90000")

    elif branch == "CE":
        print("\nYOU HAVE CHOSEN CIVIL ENGINEERING")
        print("Fee per year = ₹85000")

    else:
        print("INVALID BRANCH")

else:
    print("OKAY THANK YOU :) VISIT AGAIN")
