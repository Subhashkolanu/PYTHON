age=int(input("Enter age : "))
if age>=5:
    seat=input("Seats available (True/False) : ").capitalize()
    if seat == "True":
        payment=(input("Payment status : ")).capitalize()
        if payment=="True":
            print("Ticket booked succesfully")
        else:
            print("Payment failed")
    else:
        print("Housefull")
else:
    print("Entry not allowed")