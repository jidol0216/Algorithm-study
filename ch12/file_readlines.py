import os
print(os.getcwd())


path  = ("C:/rokey/python/ch12/file1.txt")
mode = "r"
f = open(path,mode, encoding="utf-8")
# for i in range(1,11):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
lines = f.readlines()
for line in lines:
    print(line,end="")





f.close()