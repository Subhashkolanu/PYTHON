from tkinter import *
root=Tk()
root.title("BMI calculator")
root.geometry("300x300")
l1=Label(root,text="Height")
l2=Label(root,text="Weight")
l1.grid(row=0,column=1)
l2.grid(row=1,column=1)
e1=Entry(root)
e2=Entry(root)
e1.grid(row=0,column=2)
e2.grid(row=1,column=2)
def bmi():
    a=float(e2.get())
    b=float(e1.get())
    bmi=a//(b)**2
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
b=Button(root,text="Calculate",command=bmi)
b.grid(row=2,column=2)
mainloop()