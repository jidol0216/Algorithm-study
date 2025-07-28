import re

p = re.compile('[a-z]+')

m = p.findall("life is too short")

print(m)


p = re.findall('[a-z]+',"life is too short")

print(p)