import requests
import json

url_address = "register/new_user/"
json_context = {'user_name' : "fuck"}


def get_method(url_address : str):
    res = requests.get(url = "http://localhost:8000/register/" + url_address)
    print("status_code [", res.status_code, "]")
    print(res.text)
    # print(type(res.text))


def post_method(url_address : str, data ):
    res = requests.post(url = "http://localhost:8000/register/" + url_address, data = data)
    print("status_code [", res.status_code, "]")
    print("response text: ", res.text)
    # print(type(res.text))

if __name__ == "__main__":
    # post_method("new_user/", json_context)
    get_method("initial_standard_buff_table/")
    # with open('./static/SBT.json') as f:
    #     data = json.loads(f.read())
    #     print(type(data))
