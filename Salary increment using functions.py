n=input("Name : ")
b=int(input("Basic salary : "))
e=int(input("Experience : "))
bo=0
def experience():
    if e>5:
        bo=b*0.20
    else:
        bo=b*(0.10)
    return bo
bonus=experience()
def total():
    t=b+bonus
    return t
total()
print("-----Salary slip-----")
print("Name :",n)
print("Basic salary :",b)
print("Experience :",e)
print("Bonus :",experience())
print("Total salary :",total())
