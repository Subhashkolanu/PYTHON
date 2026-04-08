class A:
    def __init__(self):
        self.x=10
    def display(self):
        print("Value :",self.x)
class B:
    def show(self):
        obj=A()
        print(obj.x)
        obj.display()
b=B()
b.show()