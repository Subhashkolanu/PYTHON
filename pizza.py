print("Enter the size of pizza (S/M/L):")
size=input()
bill=0
if size=='s' or size=='S':
    bill=bill+150
    print('Do you want pepper?')
    pepper=input()
    if pepper=='yes' or pepper=='Yes':
        bill=bill+30
        print('Do you want extra cheese ? ')
        cheese=input()
        if cheese=='yes' or cheese=='Yes':
            bill=bill+50
            print("Your total is",bill)
        else:
            print("Your total is",bill)
    else:
        print("Your total is",bill)
    if bill>400:
        bill//100*10
elif size=='m' or size=="M":
    bill=bill+250
    print('Do you want pepper?')
    pepper=input()
    if pepper=='yes' or pepper=='Yes':
        bill=bill+50
        print('Do you want extra cheese ? ')
        cheese=input()
        if cheese=='yes' or cheese=='Yes':
            bill=bill+50
            print("Your total is",bill)
        else:
            print("Your total is",bill)
    else:
        print("Your total is",bill)
        if bill>400:
            bill//100*10
elif size=='M' or size=='m':
    bill=bill+350
    print('Do you want pepper?')
    pepper=input()
    if pepper=='yes' or pepper=='Yes':
        bill=bill+30
        print('Do you want extra cheese ? ')
        cheese=input()
        if cheese=='yes' or cheese=='Yes':
            bill=bill+50
            print("Your total is",bill)
        else:
            print("Your total is",bill)
    else:
        print("Your total is",bill)
        if bill>400:
            bill//100*10