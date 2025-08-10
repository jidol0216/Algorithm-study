import os
from pathlib import Path

def list_text_files(folder_path):
    """
    특정 폴더에서 모든 .txt 파일을 검색하여 리스트로 반환
    :param folder_path: 검색할 폴더 경로
    :return: .txt 파일 리스트
    """
    f_list = []
    files = os.listdir(folder_path)
    for file in files:
        if file[-4:] == ".txt":
            f_list.append(file)
    return f_list

if __name__ == "__main__":
    folder = f"./ch22/assignment/sample_folder"
    if not os.path.exists(folder):
        os.mkdir(folder)  # 디렉토리 생성

    file1 = f"{folder}/file1.txt"
    file2 = f"{folder}/file2.txt"

    with open(file1, "w") as f:
        f.write("file1\n")
    with open(file2, "w") as f:
        f.write("file2\n")

    source = "./ch22/manage_file/folder1"
    print(".txt 파일 목록:", list_text_files(source))
