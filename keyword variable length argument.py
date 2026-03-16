def class_room_details(**d):
    for k,v in d.items():
        print(k,v,sep=" : ")
    return
class_room_details(Block="University",Floor=1,Section="cse-6",Room_no=202)