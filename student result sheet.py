class student:
    def __init__(self,roll_number,name,ap,res):
        self.rn=roll_number
        self.nm=name
        self.app=ap
        self.r=res
    def getdet(self):
        print("Name : ",self.nm)
        print("Roll number : ",self.rn)
        print("Attendance : ",self.app)
        print("CGPA/SGPA : ",self.r)
n=input("Enter name : ")
u=int(input("Enter roll number : "))
e=float(input("Enter attendance percentage : "))
c=float(input("CGPA/SGPA : "))
s=student(n,u,e,c)
s.getdet()