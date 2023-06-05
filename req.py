import requests
ip = ''
api_key = ''
url = f'https://api.ip2location.io/?key={}&ip={ip}'
response = requests.get(url)
print(response.status_code)
if response.status_code == 200:
    data = response.json()
    print(data)
    if (data['country_code'] == 'KR'):
      print("whitelisted kr")
