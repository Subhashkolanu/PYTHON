with open("source_audio.mp3","rb") as src:
    data=src.read()
with open("destination_audio.mp3","wb") as dist:
    dist.write(data)
print("Song transferred succesfully!")
import os
os.startfile("destination_audio.mp3")