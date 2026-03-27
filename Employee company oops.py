class Employee:
    company="XYZ solutions"
    def __init__(self,name,salary):
        self.nm=name
        self.sal=salary
    def getdetails(self):
        print("Employee name :",self.nm)
        print("Salary :",self.sal)
        print("Company :",Employee.company)
n=input("Enter name : ")
s=int(input("Enter salary : "))
print("-----Employee Details-----")
e=Employee(n,s)
e.getdetails()
