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
    if p>=75:
        print("Eligible")
    else:
        print("Not eligible")