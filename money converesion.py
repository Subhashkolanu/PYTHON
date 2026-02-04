r=int(input("Enter the ammount of rupees : "))
print('''select the currency to exchange : 
1. Dollar
2. Pound
3. Yen
4. Euro''')
choice = int(input("Enter your choice (number) : "))
if choice == 1 :
    Dollar=r//90
    print("For exchange of",r,"you have",Dollar,"$")
if choice == 2 :
    Pound=r//120
    print("For exchange of",r,"you have",Pound,"£")
if choice == 3:
    Yen = r//0.60
    print("For exchange of",r,"you have",Yen,"¥")
if choice == 4 :
    Euro=r//105
    print("For exchage of",r,"you have",Euro,"€")