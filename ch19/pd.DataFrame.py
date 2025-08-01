import pandas as pd

data=[
    [1,"alice",30],
    [2,"bob",35],
    [3,"charlie",25]


]

dataF =pd.DataFrame(data,columns=["Id","Name","Age"])

print(dataF)


print(type(dataF))


