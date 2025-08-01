import pandas as pd

df_csv =pd.read_csv("ch19\data.csv")
print(df_csv)

'Hr'
data = {"ID":[1,2,3,4,5,6],
        "Department":["HR","Engineering","Sales","R&D","Finance","Planning"]}

df3 = pd.DataFrame(data)
merged = pd.merge(df3)

print(merged)