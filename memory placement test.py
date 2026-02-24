'''c=5
d=10
print(id(c))
print(id(d))
loc_1 = id(c)
loc_2 = id(d)
if loc_1==loc_2:
    print("Both are placed at same location")
else:
    print("Both are placed at diffirent locations")
e=20
f=20
print(id(e))
print(id(f))
loc_3 = id(e)
loc_4 = id(f)
if loc_3==loc_4:
    print("Both are placed at same location")
else:
    print("Both are placed at diffirent locations")'''
'''OR'''
a=int(input('Enter integer 1 : '))
b=int(input('Enter integer 2 : '))
print(id(a))
print(id(b))
if a is b:
    print('True')
else:
    print('False')