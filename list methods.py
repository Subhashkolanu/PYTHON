l=['Java','Python','C','C++','c#']
x=['BMW','AUDI','TOYOTA','FIAT','LEXUS']
n = ["sai", "rahul", "anil", "pavan", "kiran"]
m = [78, 92, 65, 88, 74, 91]
c=[]
print("Original language list : ",l)
print("Original cars list : ",x)
print("Original names list : ",n)
print("Original integers list : ",m)
x.append("BENZ")
print("Method append : ",x)
m.sort()
print("Method sort : ",m)
m.reverse()
print("Method reverse : ",m)
n.insert(5,"subhash")
print("Method insert : ",n)
n.extend(m)
print("Method extend : ",n)
n.remove("rahul")
m.remove(88)
print("Method remove : ",n,m)
c=x.copy()
print("Method copy : ",c)
c.clear()
print("Method clear : ",c)
ca=x.count("BENZ")
print("Method count : ",ca)