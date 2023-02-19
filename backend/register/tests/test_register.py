from django.test import TestCase
from django.test import Client
from .unity import output_checked_out

# Create your tests here.
class register_init_test(TestCase):

    # @output_checked_outs
    def test_register_new_user(self):
        url_address = "new_user/"
        data = {'user_name' : "111"}
        return Client().get("/register/" + url_address)

        
    # @output_checked_out
    def test_reset_registered_user(self):
        url_address = "reset_registered_user/"
        return Client().get("/register/" + url_address)



   