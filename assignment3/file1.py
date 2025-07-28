
with open("data.txt", "w", encoding="utf-8") as f:
    for i in range(1, 11):
        f.write(f"{i}번째 줄입니다.\n")



with open("data.txt",'a',encoding="utf-8") as f:
    f.write("11번째 줄입니다.\n")
    
with open("data.txt", "r", encoding="utf-8") as f:
    contents = f.read()
    print(contents)
