import pandas as pd

data = [1,2,3]

series = pd.Series(data)
print(series)

data = {"a":10, "b":20,"c":30}

series = pd.Series(data)
print(series)
print(type(series))
