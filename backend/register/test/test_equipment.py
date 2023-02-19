from django.test import TestCase
from .unity import get_method, post_method

# Create your tests here.
class register_init_test(TestCase):

    def test_initial_standard_equipments_table(self):
        url_address = "initial_standard_equipments_table/"
        get_method(url_address)

    def test_reset_registered_user(self):
        url_address = "get_all_standard_equipments/"
        get_method(url_address)


