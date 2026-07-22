# These are also called as conditional expressions
#x if condition is true else y

#Easy
age=int(input("Enter age : "))
print("Eligible for voting" if age>=18 else "Not eligible")

#Medium
a=int(input("Enter number 1 : "))
b=int(input("Enter number 2 : "))
print(a if a>b else b)

#Hard
marks=int(input("Enter marks (max:100) : "))
print("A" if marks>=90 else 
      "B" if marks>=80 else 
      "C" if marks>=70 else 
      "D" if marks>=60 else 
      "E" if marks>=50 else
      "F")

#Extra hard
a=int(input("Enter number 1 : "))
b=int(input("Enter number 2 : "))
c=int(input("Enter number 3 : "))
print(a if a>b and a>c else b if b>a and b>c else c)
