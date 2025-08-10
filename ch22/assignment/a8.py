from pathlib import Path

folder_path = Path(r"C:/rokey/python/ch22/assignment/new_folder")

folder_path.mkdir(exist_ok=True)

print(f"'{folder_path}' 폴더가 생성되었거나 이미 존재합니다.")
