import os
if os.path.exists("abc.txt"):
    print("File Found!")
    ask=input("Remove (Y/n)")
    if ask=="Y":
        os.remove("abc.txt")
        print("File deleted.")
    else:
        print("File is not removed")
else:
    print("File not found")