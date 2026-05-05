filename=input()
try:
    file=open(filename,"r")
    emails=file.readlines()
    file.close()
    emails=[email.strip() for email in emails]
    result=";".join(emails)
    print(result)
except FileNotFoundError:
    print("not found")