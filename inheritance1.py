class Faculty:
    def __init__(self,fac_name,fac_age):
        self.nm=fac_name
        self.age=fac_age
    def displaydetails(self):
        print("Faculty name :",self.nm)
        print("Age :",self.age)
class Facultydetails(Faculty):
    def __init__(self,fac_name,fac_age,fac_sub,fac_sal):
        super().__init__(fac_name,fac_age)
        self.sub=fac_sub
        self.sal=fac_sal
    def getdetails(self):
        print("Subject :",self.sub)
        print("Salary :",self.sal)
n=input("Enter name : ")
a=int(input("Enter age : "))
s=input("Enter subject : ")
sa=int(input("Enter salary : "))
f=Facultydetails(n,a,s,sa)
f.displaydetails()
f.getdetails()