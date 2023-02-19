from django.test import TestCase
from django.test import Client
from .unity import output_checked_out

# Create your tests here.
class register_init_test(TestCase):

    # @output_checked_out
    def test_initial_standard_equipments_table(self):
        url_address = "initial_standard_equipments_table/"
        return Client().get("/register/" + url_address)

    def test_reset_registered_user(self):
        url_address = "get_all_standard_equipments/"
        return Client().get("/register/" + url_address)


