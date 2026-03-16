add=lambda a,b:a+b
n1=int(input("n1 : "))
n2=int(input("n2 : "))
print("Sum : ",add(n1,n2))
even_or_odd_n=lambda n:print("Even") if n%2==0 else print("Odd")
even_or_odd_n(n1)
even_or_odd_n(n2)