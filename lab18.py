import os
def copy_file(source_file,target_file):
    with open (source_file,"r") as src:
        data=src.read()
    with open(target_file,"w") as tgt:
        tgt.write(data)
source_file=input()
target_file=input()
copy_file(source_file,target_file)
if os.path.getsize(target_file)==0:
    print("Content not copied")
else:
    print("Content copied")