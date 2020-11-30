import requests
from api_validation.payload import *
from utilities.configurations import *
from utilities.resourses import *
from bdd.features.steps import *


def after_scenario(context, scenario):
    if 'library' in scenario.tags:
        context.book_id = context.response_dict['ID']
        header_del = {'ID': context.book_id}
        delete_book_url = get_config()['API']['endpoint'] + ApiResourses.delete_book
        delete_book_response = requests.post(delete_book_url, json=header_del, headers=context.header)
        response_dict_delete = delete_book_response.json()

        print(delete_book_response.status_code)
        assert delete_book_response.status_code == 200
        print(response_dict_delete['msg'])
        assert response_dict_delete['msg'] == 'book is successfully deleted'
