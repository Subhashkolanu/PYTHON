print('''Available platforms
1. Netflix - Rs.499
2. Amazon Prime - Rs.399
3. Disney+ Hotstar - Rs.299
4. AHA - Rs.199
5. Zee5 - Rs.149
''')
dis=0
amt=0
print("How many OTT platforms do you want to select (1/2/3) : ")
ott=int(input())
if ott>3:
    print("You can select only three at a time.")
elif ott>=1:
    print('Enter your choice one :')
    ch1=int(input())
    if ch1==1:
        amt=amt+499
    elif ch1==2:
        amt=amt+399
    elif ch1==3:
        amt=amt+299
    elif ch1==4:
        amt=amt+199
    elif ch1==5:
        amt=amt+149
elif ott>=2:
    print("Enter your choice two : ")
    ch2=int(input())
    if ch2==1:
        amt=amt+499
    elif ch2==2:
        amt=amt+399
    elif ch2==3:
        amt=amt+299
    elif ch2==4:
        amt=amt+199
    elif ch2==5:
        amt=amt+149
elif ott==3:
    print("Enter you choice three : ")
ch3=int(input())
if ch3==1:
    amt=amt+499
elif ch3==2:
    amt=amt+399
elif ch3==3:
    amt=amt+299
elif ch3==4:
    amt=amt+199
elif ch3==5:
    amt=amt+149
print("Final ammount",amt)
if ott==1:
    dis=0
elif ott==2:
    dis=0.30
elif ott==3:
    dis=0.40
dis_amt=amt*dis
amt_aftdis=amt-dis_amt
gst=amt_aftdis*0.20
fin_amt=amt_aftdis+gst
print('''Bill summary''')
print("No of OTT's selected : ",ott)
print("Base amount : ",amt)
print("Discount Amount: Rs.",dis_amt)
print("GST Amount (20%): Rs.", round(gst))
print("Final Payable Amount: Rs.", round(fin_amt))
