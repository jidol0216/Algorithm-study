import os
print(os.getcwd())


path  = ("C:/rokey/python/ch12/file1.txt")
mode = "w"
f = open(path,mode, encoding="utf-8")
for i in range(11,21):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)





f.close()