import os

folder_path = r"homework\logfile.log"


os.makedirs(folder_path, exist_ok=True)

path = os.path.join(folder_path, "logfile.log")

with open(path, "w", encoding="utf-8") as file:
    file.write("2025-03-30 12:00:01 INFO 서버 시작됨\n")
    file.write("2025-03-30 12:05:12 ERROR 데이터베이스 연결 실패\n")
    file.write("2025-03-30 12:10:35 WARNING 응답 속도 저하\n")
    file.write("2025-03-30 12:15:45 ERROR 사용자 인증 실패\n")

with open(path, "r", encoding="utf-8") as file:
    for line in file:
        if "2025-03-30" in line:
            print(line.strip())
