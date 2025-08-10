import requests

url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(url)


data = response.json() 
print(data)
