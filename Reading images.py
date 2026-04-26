with open ("Brosan.jpg","rb") as img:
    image=img.read()
with open ("Image.jpg","wb") as file:
    file.write(image)
import os
os.startfile("Image.jpg")