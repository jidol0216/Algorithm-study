import re

data = "- 이메일을 입력하세요: user@example.com"


p = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._]+.[a-zA-Z]{2,}",data)


print(p)