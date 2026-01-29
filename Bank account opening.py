print("Welcome to STATE FEDARAL BANK OF INDIA ")
login = input('''select login type
      1.Sign in
      2.Sign up''')
if login == "1":
    ac_no = int(input("Enter your account number : "))
    password = input("Enter your password : ")
    if password == ac_no:
        print("Welcome user ",ac_no)
    else:
        print("Incorrect password/Acount number")
elif login == "2":
    new_ac = input("create new account? Y/n")
    if new_ac == "Y":
        name=input("Enter your name : ")
        dob=int(input("Enter age : "))
        if dob>=18:
            print("You are eligible for Savings account")
            import random
            new_ac_no = random.randint(10000000,100000000)
            print("Your bank account no is ",new_ac_no)
            add = input("Enter your address : ")
            gen_otp = random.randint(100000, 999999)
            print("Enter your otp:")
            print("Your OTP is:", gen_otp)
            otp = int(input("Enter your otp: "))
            if otp == gen_otp:
                print('''You have been successfully verified 
              You will recieve the pin to your address''',add)
            else:
                print("Wrong OTP")
        else:
            print("You are not eligible for Savings account")
else:
    print("Request timed!")