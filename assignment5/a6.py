import os

file_path = r"C:\rokey\python\assignment5\config.ini"

config = {}
with open(file_path, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line or "=" not in line:
            continue
        key, value = line.split("=", 1)
        config[key.strip()] = value.strip()

print(config)
