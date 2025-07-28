import re

p = re.compile('[a-z]+')

m = p.findall("life is too short")

print(m)