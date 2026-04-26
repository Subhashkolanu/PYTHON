with open("Para.txt") as file:
    content=file.read()
lines=content.split("\n")
print("Lines :",lines)
words=content.split()
print("Words :",words)
print("Characters :",len(content))