import os


ini_path = r"C:\rokey\python\assignment5\config.ini"


folder = os.path.dirname(ini_path)
os.makedirs(folder, exist_ok=True)

with open(ini_path, "w", encoding="utf-8") as f:
    f.write("1반 = 홍길동\n")
    f.write("2반 = 김철수\n")
    f.write("3반 = 박영희\n")
    f.write("4반 = 최로키\n")

print("config.ini 파일이 생성되었습니다.")
