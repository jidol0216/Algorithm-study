import pandas as pd
import matplotlib.pyplot as plt
csv_path = r"C:\rokey\python\assignment4\대구광역시 동구_연도별 체납차량 번호판 영치실적_20241201.csv"
df = pd.read_csv(csv_path, encoding="euc-kr")


df_filtered = df[(df['년도'] >= 2016) & (df['년도'] <= 2024)]


plt.figure(figsize=(10,6))
plt.plot(df_filtered['년도'], df_filtered['영치대수'], marker='o', color='blue', linestyle='-')
plt.title('2016년부터 2024년까지 연도별 영치대수')
plt.xlabel('년도')
plt.ylabel('영치대수')
plt.xticks(df_filtered['년도'])
plt.grid(True)
plt.show()
