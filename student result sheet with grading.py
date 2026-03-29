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
    def grade(self):
        if self.r >= 7.0:
            print("Grade A")
            print("Promoted")
        elif self.r >= 6.5:
            print("Grade B")
            print("Promoted")
        elif self.r >= 6.0:
            print("Grade C")
            print("Promoted")
        elif self.r >= 5.5:
            print("Grade D")
            print("Promoted")
        else:
            print("Failed")

n=input("Enter name : ")
u=int(input("Enter roll number : "))
e=float(input("Enter attendance percentage : "))
c=float(input("CGPA/SGPA : "))
s=student(u,n,e,c)
print("-----Result sheet-----")
s.getdet()
s.grade()