import json

ini_path = r"C:\rokey\python\assignment5\config.ini"
json_path = r"C:\rokey\python\assignment5\config.json"


config = {}
with open(ini_path, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line or "=" not in line:
            continue
        key, value = line.split("=", 1)
        config[key.strip()] = value.strip()


with open(json_path, "w", encoding="utf-8") as f:
    json.dump(config, f, ensure_ascii=False, indent=4)

print(f"JSON 파일이 '{json_path}'에 저장되었습니다.")
