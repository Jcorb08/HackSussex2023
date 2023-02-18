import requests
url_address = "http://localhost:8000/register/new_user/"
json_context = {'user_name' : "fuck"}
res = requests.post(url = url_address, data = json_context)
print("status_code [", res.status_code, "]")
print(res.text)
# print(type(res.text))