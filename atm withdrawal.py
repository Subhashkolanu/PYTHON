registered_pin=1234
pin=int(input("Enter your pin : "))
if pin == registered_pin:
    balance=int(input("enter balance : "))
    ammount=int(input("Enter ammount to withdraw : "))
    if balance>ammount:
        print("Transaction succesful")
    else:
        print("Insufficient balance")
else:
    print("Incorrect pin")