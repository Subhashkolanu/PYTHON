class shape:
    def area(self):
        print("This is not for generic shapes")
class rectangle:
    def __init__(self,length,breadth):
        self.len=length
        self.bre=breadth
        print("Area of rectangle :",self.len*self.bre)
class circle:
    def __init__(self,radius):
        self.r=radius
        print("Area of circle :",3.14*self.r*self.r)
l=float(input("Enter length : "))
b=float(input("Enter breadth : "))
ar=rectangle(l,b)

r=float(input("Enter radius : "))
ac=circle(r)