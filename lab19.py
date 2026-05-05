from pandas import *
data = {
 'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank',
'Grace', 'Hannah', 'Ian', 'Julia'],
 'Age': [25, 30, 22, 28, 24, 27, 29, 23, 26, 31],
 'Department': ['HR', 'Finance', 'IT', 'HR', 'Finance', 'IT', 'HR',
'Finance', 'IT', 'HR'],
 'Salary': [50000, 60000, 55000, 52000, 61000, 53000, 58000, 62000,
54000, 57000],
 'Experience': [2, 4, 1, 3, 2, 2, 5, 4, 3, 6]
}
df=DataFrame(data)
print(df.head())
print(df[["Name","Salary"]])
print(df[df["Age"]>25])
print(df[df["Department"]=="IT"])
print(df[(df["Age"]>25) & (df["Salary"]>55000)])