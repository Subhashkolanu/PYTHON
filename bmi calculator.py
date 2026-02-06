print("Enter weight in kg's :")
weight=float(input())
print("Enter height in meters :")
height=float(input())
bmi=weight//height**2
if bmi<18.5:
    print('Your bmi is',bmi,'Underweight')
elif bmi<25:
    print('Your bmi is',bmi,'Normal weight')
elif bmi<30:
    print('Your bmi is',bmi,'Overweight')
elif bmi<35:
    print('Your bmi is',bmi,'obese')
else:
    print('Consult a doctor immediately')