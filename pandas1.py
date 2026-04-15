import pandas as s
l1=s.Series([10,20,30,40,"KSS"]) #object 
l2=s.Series("say my name") #str
l3=s.Series([0.5,0.2,0.9]) #float
print(l1)
print(l2)
print(l3)
print("Values of list 1 :",l1.values)
print("Values of list 2 :",l2.values)
print("Values of list 3 :",l3.values)