import os
print(os.getcwd())


path=r"c:\rokey\python\ch12\file\계좌1.txt"
mode = "r"
account_list=[]

with open(path,mode,encoding="utf-8") as fa:
    na=fa.readlines()
    for i in na:
        if ':' in i:
            key,Value = i.strip().split(":")
            account_list.append(Value)
    print(account_list)