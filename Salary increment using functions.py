n=input("Name : ")
b=int(input("Basic salary : "))
e=int(input("Experience : "))
bo=0
def experience():
    if e>5:
        bo=b*(20/100)
        print("Bonus : ",bo)
    else:
        bo=b*(10/100)
        print("Bonus : ",bo)
    return bo
bonus=experience()
def total():
    t=b+bonus
    print("Total salary : ",t)
    return
total()
