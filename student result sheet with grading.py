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
s=student(u,n,e,c)
print("-----Result sheet-----")
s.getdet()
if c>7.0:
    print("GRADE A")
    print("Promoted to next semester")
elif c>6.5 and c<7.0:
    print("GRADE B")
    print("Promoted to next semester")
elif c>6.0 and c<6.5:
    print("GRADE c")
    print("Promoted to next semester")
elif c>5.5 and c<6.0:
    print("GRADE D")
    print("Promoted to next semester")
else:
    print("Failed")
if e<75:
    print("Result delared with Fine for attendance")