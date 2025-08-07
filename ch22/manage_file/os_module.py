import os

print(f"현재 작업 디렉터리:{os.getcwd()}")

os.chdir(r"ch22\manage_file")
print(f"변경된 작업 디렉터리:{os.getcwd()}")
print("-------------------------------------")
# print(f"디렉터리 목록:{os.listdir(".")}")
os.rmdir("test_dir")

os.mkdir("test_dir")


if os.path.exists("file.txt"):
    print("파일 있음")
    
    
    
    
print("------------------------------------")


folder = os.getcwd()

print(os.path.join(folder,"file.txt"))
print(os.path.basename(f"{folder}/file.txt"))
print(os.path.dirname(f"{folder}/file.txt"))