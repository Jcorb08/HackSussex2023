import requests

url_address = "register/new_user/"
json_context = {'user_name' : "fuck"}


def get_method(url_address : str):
    res = requests.get(url = "http://localhost:8000/register/" + url_address)
    print("status_code [", res.status_code, "]")
    print(res.content)
    # print(type(res.text))


def post_method(url_address : str, data ):
    res = requests.post(url = "http://localhost:8000/register/" + url_address, data = data)
    print("status_code [", res.status_code, "]")
    print("response text: ", res.text)
    # print(type(res.text))

test_list = ['new_user/', 'reset_registered_user/', 'initial_standard_buff_table', 'initial_standard_equipments_table', 'get_all_standard_equipments']
# 'new_user/'


if __name__ == "__main__":

    # for test_case in test_list:
    #     get_method(test_case)
    # post_method('post_for_equipment_card/', {'user_id':2})
    # post_method('post_new_user/', {'user_name':'user5'})
    # get_method('get_for_equipment_name/')
    # post_method('post_for_attack_shark/', {'equipment_name':'Stick', 'shark_id':1})
    # get_method('get_initial_shark/')
    get_method('get_shark_hp')

