name = input("Enter your name : ")
print("\nHello", name, "! Welcome to VVITU")
int_marks = int(input("\nEnter your INTERMEDIATE marks : "))
jee_per = int(input("Enter your JEE percentile : "))

# checking eligibility
if int_marks >= 750 or jee_per >= 80:
    print("\nYOU ARE ELIGIBLE FOR ADMISSION :)")
    admission = "Y"
    merit="Y"
else:
    print("\nYOU ARE NOT ELIGIBLE FOR ADMISSION :(")
    merit="N"
    #Mangement quota
    admission = input("\nEnter your choice (MANAGEMENT) Y/N : ").upper()
    if admission == "Y":
        print("These are the courses offered here")
        print("1. CSE")
        print("2. ECE")
        print("3. EEE")
        print("4. ME")
        print("5. CE")
        branch = input("Choose branch : ").upper()
        if branch == "CSE":
            s=input("Specialisation : Y/n : ").upper()
            if s=="Y":
                print("Specialisations available:")
                print("1. AI-ML")
                print("2. AI-DS")
                print("3. CYBER SECURITY")
                spec = input("Choose your specialisation : ").upper()
                if spec == "AI-ML":
                    print("\nSeat has been allotted in CSE-AI-ML")
                    print("Fee per year = ₹180000")

                elif spec == "AI-DS":
                    print("\nSeat has been allotted in CSE-AI-DS")
                    print("Fee per year = ₹140000")

                elif spec == "CYBER SECURITY":
                    print("\nSeat has been allotted in CSE-CYBER SECURITY")
                    print("Fee per year = ₹150000")

                else:
                    print("INVALID SPECIALISATION")
            else:
                print("YOU HAVE CHOOSEN CSE")
                print("\nSeat has been allotted in CSE-CORE")
                print("Fee per year = ₹135000")

        elif branch == "ECE":
            print("\nYOU HAVE CHOSEN ECE")
            print("Fee per year = ₹130000")

        elif branch == "EEE":
            print("\nYOU HAVE CHOOSEN EEE")
            print("Fee per year = ₹110000")

        elif branch == "ME":
            print("\nYOU HAVE CHOOSEN MECHANICAL ENGINEERING")
            print("Fee per year = ₹110000")

        elif branch == "CE":
            print("\nYOU HAVE CHOOSEN CIVIL ENGINEERING")
            print("Fee per year = ₹100000")

        else:
            print("INVALID BRANCH")
#Merit quota
if admission == "Y" and merit == "Y":
    print("These are the courses offered here")
    print("1. CSE")
    print("2. ECE")
    print("3. EEE")
    print("4. ME")
    print("5. CE")

    branch = input("Choose branch : ").upper()

    if branch == "CSE":
        s=input("Specialisation : Y/n : ").upper()
        if s=="Y":
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
        else:
            print("\nSeat has been allotted in CSE-CORE")
            print("Fee per year = ₹125000")


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
