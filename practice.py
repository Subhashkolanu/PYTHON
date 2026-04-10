class Animal:
    def show(self):
        print("Dog")

class wild(Animal):
    def show(self):
        print("Tiger")

class C(Animal):
    def show(self):
        print("C")

class D(wild, C):
    pass

obj = D()
obj.show()