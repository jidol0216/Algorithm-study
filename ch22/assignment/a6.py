import os

folder_path = r"C:\rokey\python\ch22\assignment\sample_folder"

if not os.path.exists(folder_path):
    print(f"'{folder_path}' 폴더가 없어 생성합니다.")
    os.makedirs(folder_path) 
else:
    print(f"'{folder_path}' 폴더가 존재합니다.")


items = os.listdir(folder_path)
print(f"'{folder_path}' 안의 파일과 폴더 목록:")
for item in items:
    print(item)
