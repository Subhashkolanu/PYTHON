file=open("mydata.txt","r")
n=int(input("Enter no of lines : "))
if n<=5:
     for i in range(n):
          print(file.readline())
else:
     print("Exceeded the value.")