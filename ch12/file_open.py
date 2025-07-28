# import os
# print(os.getcwd())



# f = open("C:/rokey/python/ch12/file1.txt", "w")

# f.close()

with open("test.txt", "w") as file:
    file.write("Hello, World!")
print(file.closed)