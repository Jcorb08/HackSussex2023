from django.test import TestCase
import requests


# Create your tests here.
class simple_test(TestCase):
    def test_post_reaponse(self):
        url_address = "http://localhost:8000/register/register_user/"
        json_context = {'user_name' : "aghfdhfdhshfsfh", 'IP_address' : "testing_user_IP"}
        res = requests.post(url = url_address, data = json_context)
        print(res.text)


   