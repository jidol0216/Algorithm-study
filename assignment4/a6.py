import pandas as pd


csv_path = r"C:\rokey\python\assignment4\대구광역시 동구_연도별 체납차량 번호판 영치실적_20241201.csv"
df = pd.read_csv(csv_path, encoding="euc-kr")



print(df.info())
print(df.head())
