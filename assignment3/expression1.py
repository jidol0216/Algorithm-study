import re



data = """python one
life is too short
python two
you need python
python three"""



p = re.findall(r'\bpython\w*',data)

print(p)
