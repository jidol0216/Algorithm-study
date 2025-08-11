import os

ini_path = r"C:\rokey\python\assignment5\config.ini"

try:
    with open(ini_path, "r", encoding="utf-8") as f:
        config = {}
        for line in f:
            line = line.strip()
            if not line or "=" not in line:
                continue
            key, value = line.split("=", 1)
            config[key.strip()] = value.strip()
except FileNotFoundError:
    folder = os.path.dirname(ini_path)
    os.makedirs(folder, exist_ok=True)

    with open(ini_path, "w", encoding="utf-8") as f:
        f.write("1반 = \n")
        f.write("2반 = \n")
        f.write("3반 = \n")
        f.write("4반 = \n")

    config = {
        "1반": "",
        "2반": "",
        "3반": "",
        "4반": ""
    }

print(config)
