from django.test import Client


def get_method(url_address : str):
    res = Client().get("/register/" + url_address)
    print("status_code [", res.status_code, "]")
    print("response content: ", res.content)

def post_method(url_address : str, data ):
    res = Client().post("/register/" + url_address, data = data)
    print("status_code [", res.status_code, "]")
    print("response content: ", res.content)