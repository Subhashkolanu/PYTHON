import random
veh = input('''choose the vehicle type :
            A.Two wheeler
            B.car
            C.Truck/Bus(Heavy vehicle) ''')
if veh == "A":
    reg_no=input("Enter the Reg no : ")
    time=int(input("Enter the no of hours : "))
    charge=time*10
    place = print("You have been alloted space at block",random.randint(1,100),"for vehicle",reg_no,"upto",time,"hours @",charge,"₹")
elif  veh == "B":
    reg_no=input("Enter the Reg no : ")
    time=int(input("Enter the no of hours : "))
    charge=time*15
    place = print("You have been alloted space at block",random.randint(1,100),"for vehicle",reg_no,"upto",time,"hours @",charge,"₹")
elif veh == "C":
    reg_no=input("Enter the Reg no : ")
    time=int(input("Enter the no of hours : "))
    charge=time*20
    place = print("You have been alloted space at block",random.randint(1,100),"for vehicle",reg_no,"upto",time,"hours @",charge,"₹")
else:
    print("Parking unavailable")