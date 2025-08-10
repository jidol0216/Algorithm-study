import requests

response = requests.get("https://randomuser.me/api/")

data = response.json()
name = data['results'][0]['name']
full_name = f"{name['title']} {name['first']} {name['last']}"
print(full_name)
