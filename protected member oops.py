class A:
    def __init__(self,Input):
        self._x=Input
    def display(self):
        print("Value of x :",self._x)
n=int(input("Enter value : "))
a=A(n)
a.display()