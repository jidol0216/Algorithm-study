import json

json_path = r"C:\rokey\python\assignment5\config.json"

with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

print(data)
