'''class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

obj = D()
obj.show()'''
file = open("sample.txt", "r")

print(file.tell())   # current position
file.seek(5)         # move cursor to index 5

print(file.read())
file.close()