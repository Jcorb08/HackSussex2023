import requests
url_address = "http://localhost:8000/register/register_user/"
json_context = {'user_name' : "aghfdhfdhshfsfh"}
res = requests.post(url = url_address, data = json_context)
print(res.status_code)
print(res.text)