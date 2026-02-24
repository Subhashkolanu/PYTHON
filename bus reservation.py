total_seat = 40
print('Enter no of seats required : ')
seat = int(input())
if seat > 1:
    print("Only one seat at a time")
else:
    print('Enter your age : ')
    age = int(input())
    print("Ticket type: (AC/Non AC)")
    ticket = input()
    ac = 800
    non = 500
    if seat <= total_seat:
        if ticket == "ac" or ticket == "AC":
            base = ac * seat
        else:
            base = non * seat
        if age >= 5 and age <= 12:
            dis = 0.50
        elif age >= 13 and age <= 18:
            dis = 0.20
        elif age >= 19 and age <= 60:
            dis = 0.00
        else:
            dis = 0.30
        base = base - (base * dis)
        print("Booking Confirmed")
        print("Final cost of the bill:", base)
    else:
        print("Booking Not Confirmed, Not Enough Seats Available")