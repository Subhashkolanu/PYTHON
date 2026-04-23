name=["Bharat","Shanmukha","Venkatesh","Anish"]
with open("newfile.txt","w") as f:
    f.writelines(name)
with open("newfile.txt","r") as file:
    for line in file:
        print(line.strip())