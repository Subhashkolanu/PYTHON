print("Enter the size of pizza (S/M/L):")
size=input()
bill=0
if size=='s' or size=='S':
    bill+=150
elif size=='m' or size=='M':
    bill+=250
elif size=='l' or size=='L':
    bill+=350
print("Add pepper? Y/N")
pepper=input()
if size=='s' or size=='S':
    if pepper=='y' or pepper=='Y':
        bill+=30
else:
    if pepper=='y' or pepper=='Y':
        bill+=50
print("Add cheese? Y/N")
cheese=input()
if cheese=='y' or cheese=='Y':
    bill+=50
if bill>400:
    bill=bill+(bill*0.10)
print("Your total bill is",bill)