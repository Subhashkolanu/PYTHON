with open ("Brosan.jpg","rb") as img:
    image=img.read()
with open ("Image.jpg","wb") as file:
    file.write(image)
print("Image data copied succesfully")
import os
os.startfile("Image.jpg")