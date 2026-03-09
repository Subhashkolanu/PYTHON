def greet():
    print("Hello!")

greet()

def cap(s):
    return s.capitalize()
s=input("data: ")
print("s :",cap(s))

def count(s):
    return s.count('@')
s=input("Enter your mail id : ")
print("Count of @ in str : ",count(s))