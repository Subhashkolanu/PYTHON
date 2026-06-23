print("""select the conversion type 
1. MB to Mb 
2. Mb to MB""")
o=int(input())
if o==1:
    MB=int(input("Enter no of megabytes (MB): "))
    MB*=8
    print("No of MegaBits (Mb): ",MB)
else:
    Mb=int(input("Enter no of megabits (Mb) : "))
    Mb/=8
    print("No of MegaBytes (MB) : ",Mb)