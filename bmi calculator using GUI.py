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
def calc():
    a=float(e2.get())
    b=float(e1.get())
    bmi=a//(b)**2
    if bmi<18.5:
        msg='Underweight'
    elif bmi<25:
        msg='Normal weight'
    elif bmi<30:
        msg='Overweight'
    elif bmi<35:
        msg='obese'
    else:
        msg='Consult a doctor immediately'
    l.configure(text=f"Result : {bmi} and {msg}")
b=Button(root,text="Calculate",command=calc)
b.grid(row=2,column=2)
l=Label(root,text=" ")
l.grid(row=3,column=2)
mainloop()