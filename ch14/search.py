import re

p = re.compile('[a-z]+')

m = p.search("3 python")
m = p.search("3 pyt8thon")
print(m)