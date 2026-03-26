class fac:
        def __init__(self,name,rn,exp):
            self.nm=name
            self.rid=rn
            self.xp=exp
        def det(self):
            print("Name : ",self.nm)
            print("Register number : ",self.rid)
            print("Experience : ",self.xp)
n=int(input("Enter no of faculty : "))
for i in range(n):
    n=input("Enter name : ")
    u=int(input("Enter register number : "))
    e=int(input("Enter experience : "))
f=fac(n,u,e)
f.det()