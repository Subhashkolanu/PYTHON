class Employee:
    company="XYZ solutions"
    def __init__(self,name,salary):
        self.nm=name
        self.sal=salary
    def getdetails(self):
        print("Employee name :",self.nm)
        print("Salary :",self.sal)
        print("Company :",Employee.company)
n1=input("Enter name : ")
s1=int(input("Enter salary : "))
n2=input("Enter name : ")
s2=int(input("Enter salary : "))
print("-----Employee 1 Details-----")
e1=Employee(n1,s1)
e1.getdetails()
print("-----Employee 2 Details-----")
e2=Employee(n2,s2)
e2.getdetails()
print("\nAfter changing the company")
Employee.company="ABC Housing board"
print("-----Employee 1 Details-----")
e1.getdetails()
print("-----Employee 2 Details-----")
e2.getdetails()