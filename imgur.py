import requests

client_id = '2492acbb0bf52fc'
client_secret = 'ab6a02254dc04b83f67fb3a9f3e6836a21339072'
headers = {'Authorization': 'Client-ID ' + client_id}
image_path = r"C:\Users\moham\Downloads\204274141_4046953665358907_2540976948710505202_n.jpg"

# Upload image
url = 'https://api.imgur.com/3/upload'
with open(image_path, 'rb') as image_file:
    response = requests.post(url, headers=headers, files={'image': image_file})

# Get link
data = response.json()
if data['success']:
    print('Image Link:', data['data']['link'])
else:
    print('Error:', data['data']['error'])
