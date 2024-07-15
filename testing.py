import requests


api_url = 'https://api.npoint.io/9424430201af096183d7'

# Fetch data from API with error handling

response = requests.get(api_url)
response.raise_for_status()
posts = response.json()

for i in posts:
    print(i.title)