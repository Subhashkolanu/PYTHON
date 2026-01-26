import random
gen_otp = random.randint(100000, 999999)
print("Your OTP is:", gen_otp)
otp = int(input("Enter your otp: "))
if otp == gen_otp:
    print("You have been successfully verified")
else:
    print("Wrong OTP")