age=int(input("Enter age : "))
if age>=5:
    seat=input("Seats available (True/False) : ")
    if seat == "True" or seat == "true":
        payment=(input("Payment status : "))
        if payment=="True" or payment == "true":
            print("Ticket booked succesfully")
        else:
            print("Payment failed")
    else:
        print("Housefull")
else:
    print("Entry not allowed")