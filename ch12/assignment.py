
file_path = "C:/rokey/python/ch12/pizza_file1.txt"


with open(file_path, mode="r", encoding="utf-8") as file:
    pizza_list = [line.strip() for line in file.readlines()]


print(pizza_list)