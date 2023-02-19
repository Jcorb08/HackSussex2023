def output_checked_out(func):
    def inner(self):
        res = func()
        print("status_code [", res.status_code, "]")
        print("response content: ", res.content)
    return inner

# def get_method(url_address : str):
#     return Client().get("/register/" + url_address)


# def post_method(url_address : str, data ):
#     return Client().post("/register/" + url_address, data = data)
