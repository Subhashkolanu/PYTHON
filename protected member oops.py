class A:
    def __init__(self):
        self._x=53
    def _display(self):
        print("Value : ",self._x)
class B(A):
    def show(self):
        obj=A()
        print("Value :",obj._x)
        obj._display
b=B()
b.show()