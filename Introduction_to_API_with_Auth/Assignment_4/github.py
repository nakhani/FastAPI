
import requests

url = "https://api.github.com/users/nakhani"


response = requests.get(url)

print(response.status_code)
response.json()