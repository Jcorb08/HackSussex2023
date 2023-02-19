from django.test import TestCase

from .unity import get_method, post_method

# Create your tests here.
class register_init_test(TestCase):

    def test_register_new_user(self):
        url_address = "new_user/"
        data = {'user_name' : "111"}
        post_method(url_address, data)

    def test_reset_registered_user(self):
        url_address = "reset_registered_user/"
        get_method(url_address)



   