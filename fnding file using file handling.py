file=input("Enter file name  or file path : ")
import os
if os.path.exists(file):
    print("File found!")
else:
    print("File not found!")