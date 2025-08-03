import pandas as pd


df = pd.read_csv("ch19\data2.csv", sep=None, engine="python")

for col in ["Age", "Salary"]:
    col in df.columns
    mean = df[col].mean()
    mx = df[col].max()
    mn = df[col].min()
    # print(f"{col} 평균: {mean}, 최댓값: {mx}, 최솟값: {mn}")

filtered = df[(df['Age'] >= 30) & (df['Salary'] >= 60000)]
print(filtered)