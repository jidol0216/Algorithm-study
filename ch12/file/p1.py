import os
print(os.getcwd())


path=r"c:\rokey\python\ch12\file\계좌1.txt"
mode = "w"
account={"김삿갓":"597-89-000089",
             "이수근":"343-64-000064",
             "박혁거세":"136-97-000097"}
with open(path,mode,encoding="utf-8") as f:
    for key,value in account.items():
        f.write(f"{key} : {value}\n")


