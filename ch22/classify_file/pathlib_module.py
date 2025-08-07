from pathlib import Path


print(Path.cwd())

folder = f"./ch22/classify_file"

path = Path(folder)

print(path.exists())
print(path.is_file())
print(path.is_dir())




print("--------------------------------------")



new_folder = f"./ch22/classify_file/new_folder"
path = Path(new_folder)