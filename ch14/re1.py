

import re

p = re.compile('[a]')
m = p.match('anana')

print(m)

p = re.compile('[a-zA-Z]')
m = p.match('D465aDsf05sdaf8ef')

print(m)



p = re.compile('[a-c]')
m = p.match('abcdefg')
print(m) 

p = re.compile('[ba][ab]')
m = p.match('abc')
print(m) 

p = re.compile('[b][a]')
m = p.match('abc')
print(m)


p = re.compile('[a][b]')
m = p.match('abc')
print(m) 


print("-------------------------------------------------------------------------")




p = re.compile('..')
m = p.match("a13c")
print(m)

p = re.compile('[가-힣]')
print(p.match("가cdefg"))

print("-------------------------------------------------------------------------")

p =re.compile("ca+t")
print(p.match("ct"))
print(p.match("cat"))
print(p.match("caaat"))
print("----------------------------------------------")
p =re.compile("ca*t")
print(p.match("ct"))
print(p.match("cat"))
print(p.match("caaat"))

p = re.compile('ca{1,3}t{3,}')

print(p.match("ctt"))
print(p.match("cattt"))
print(p.match("caatttt"))
print(p.match("caaatt"))


