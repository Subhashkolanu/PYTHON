class person:
    def __init__(self,name,age):
        self.nm=name
        self.a=age
    def displaydetails1(self):
        print("Name :",self.nm)
        print("Age :",self.a)
        
class Employee(person):
    def __init__(self,name,age,employee_id,salary):
        super().__init__(name,age)
        self.empc=employee_id
        self.sal=salary
    def displaydetails2(self):
        print("Employee id :",self.empc)
        print("Salary :",self.sal)
n=input("Enter name : ")
a=int(input("Enter age : "))
e=int(input("Enter Employee id : "))
s=int(input("Enter salary : "))
e1=Employee(n,a,e,s)
e1.displaydetails1()
e1.displaydetails2()