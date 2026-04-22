import pandas as pd
data={
    "Name":["KB","KSV","KV","KA","KSS"],
    "Age":[18,17,17,17,18],
    "Marks":[99,98,97,99,94]
    }
d=pd.DataFrame(data)
print(d)
d.to_csv("Marks.csv")