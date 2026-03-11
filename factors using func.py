def number_of_factors(num):
    nf=0
    for i in range(1,num+1):
        if num%i==0:
            nf+=1
        return nf
    
n=int(input("Integer : "))
print("Factors : ",number_of_factors(n))