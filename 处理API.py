import requests
url = 'http://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url, timeout = 20000)
print("status code:", r.status_code)
response_dict = r.json()
print(response_dict.keys())
