class Bankacount:
    def __init__(self,Account_Holder_Name,Account_No,Balance):
        self.ac=Account_Holder_Name
        self.ac_no=Account_No
        self.bal=Balance
    def displaydetails(self):
        print("Welcome! ",self.ac)
        print("Account no : ",self.ac_no)
        print("Balance : ")
    def credit(self):
        c=int(input("Enter amount : "))
        self.bal+=c
        print("Ammount credited! /n current balance : ",self.bal)
    def debit(self):
        d=int(input("Enter amount : "))
        if d>=self.bal:
            print("Insufficient amount to withdraw")
        else:
            self.bal-=d
            print("Ammount debited! /n current balance : ",self.bal)

