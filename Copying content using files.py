#copying content from one file to another
with open("Source.txt","r") as src:
    content=src.read()
with open ("destination.txt","w") as dest:
    copy=dest.write(content)
print("Content copied succesfully!")
import os
os.startfile("destination.txt")