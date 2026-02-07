total_seat=40
seat=0
if seat>1:
    print("Only one seat at a time ")
else:
    print('Enter your age : ')
    age=int(input())
    print("Ticket type: (AC/Non AC)")
    ticket=input()
    ac=800
    non=500
    if seat<=total_seat:
        if ticket=="ac" or ticket=='AC':
            base=ac*seat
        else:
            base=non*seat