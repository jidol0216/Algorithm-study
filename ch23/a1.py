import json


data = {
    "name": "홍길동",
    "age": 25,
    "city": "서울"
}
file_path = r"C:/rokey/python/ch23/data.json"

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
