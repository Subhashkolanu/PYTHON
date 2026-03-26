class Bankacount:
    def __init__(self,Account_Holder_Name,Account_No,Balance):
        self.ac=Account_Holder_Name
        self.ac_no=Account_No
        self.bal=Balance
    def displaydetails(self):
        print("Welcome!",self.ac)
        print("Account no :",self.ac_no)
        print("Balance :",self.bal)
    def credit(self):
        c=int(input("Enter amount to credit : "))
        self.bal+=c
        print("Ammount credited!")
        print("current balance :",self.bal)
    def debit(self):
        d=int(input("Enter amount to debit: "))
        if d>=self.bal:
            print("Insufficient amount to withdraw")
        else:
            self.bal-=d
            print("Ammount debited!")
            print("current balance :",self.bal)
n=input("Enter user name : ")
ac=int(input("Enter account number : "))
balance=int(input("Enter balance : "))
user=Bankacount(n,ac,balance)
user.displaydetails()
print("1.Credit 2.Debit")
ch=int(input())
if ch==1:
    user.credit()
elif ch==2:
    user.debit()
else:
    print("Timed out!")
