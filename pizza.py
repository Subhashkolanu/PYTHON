print("Enter the size of pizza (S/M/L):")
size=input()
bill=0
if size=='s' or size=='S':
    bill=bill+150
elif size=='m' or size=="M":
    bill=bill+250
elif size=='l' or size=='L':
    bill=bill+350
print("Add pepper? Y/n")
pepper=input()
if size=='s' or size=="S":
    if pepper=='y' or pepper=='Y':
        bill=bill+30
else:
    if pepper=="y" or pepper=='Y':
        bill=bill+50
print("Add cheese? Y/n")
cheese=input()
if cheese=='y' or cheese=='Y':
    bill=bill+50
if bill>400:
    bill=(bill*10)/100
    print(bill)
else:
    print('Your total bill is',bill)