age=int(input("Enter your age : "))
if age>=18:
    print("Do you have Indian citizenship?")
    citizenship=input()
    if citizenship=="yes":
        print("Eligible for vote.")
    else:
        print("person does not belong to India,so not eligible")
else:
    print("Under age not eligible for voting")