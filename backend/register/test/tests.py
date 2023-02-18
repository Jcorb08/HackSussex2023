from django.test import TestCase
from django.test import Client

# Create your tests here.
class simple_test(TestCase):
    def test_post_reaponse(self):
        c = Client()
        url_address = "/register/new_user/"
        data = {'user_name' : "111"}
        res = c.post(url_address, data)
        print("status_code [", res.status_code, "]")
        print(res.content)

   