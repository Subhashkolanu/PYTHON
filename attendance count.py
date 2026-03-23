t=100
min=75
a={}
s=int(input("Enter no of students : "))
for i in range(s):
    n=input("Enter name of the student : ")
    at_day=int(input("Enter total no of days present : "))
    a[n]=at_day
for student,days in a.items():
    p=(days/t)*100
    i=0
    e=0
    if p>=75:
        print("Eligible")
        e=e+1
    elif p<75:
        print("Not eligible")
        i=i+1
print("Total no of eligible students : ",e)
print("Total no of ineligble students : ",i)