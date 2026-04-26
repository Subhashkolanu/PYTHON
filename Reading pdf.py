with open("source_pdf.pdf","rb") as src:
    data=src.read()
with open("destination_pdf.pdf","wb") as dist:
    dist.write(data)
print("pdf data transferred succesfully!")
import os
os.startfile("destination_pdf.pdf")