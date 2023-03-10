import requests

url = 'https://www.ftvnews.com.tw'
headers = {
    'User-Agent': 'Thisisverycool'
}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    html = response.text
    print(html)
else:
    print('Error: cannot fetch content from', url)