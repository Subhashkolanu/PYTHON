class A:
    def __init__(self,Input):
        self.__x=Input
    def display(self):
        print("Value of x :",self.__x)
n=int(input("Enter value : "))
a=A(n)
a.display()