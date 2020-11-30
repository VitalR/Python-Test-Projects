import requests
import configparser
from api_validation.payload import *
from utilities.configurations import *
from utilities.resourses import *
from behave import *


# Books API Verification
@given('the Book details which needs to be added to Library')
def step_implementation(context):
    context.header = {'Content-Type': 'application/json;charset=UTF-8'}
    context.add_book_url = get_config()['API']['endpoint'] + ApiResourses.add_book
    context.js_payload = add_book_payload(get_rand_str(), get_rand_num())


@when('we execute the AddBook PostAPI method')
def step_impl(context):
    context.response = requests.post(context.add_book_url, json=context.js_payload,
                                     headers=context.header)


@then('book is successfully added')
def step_impl(context):
    print(context.response.json())
    context.response_dict = context.response.json()
    context.book_id = context.response_dict['ID']
    print(context.book_id)
    assert context.response.status_code == 200
    assert context.response_dict['Msg'] == 'successfully added'


@given('the Book details with {isbn} and {aisle}')
def step_implementation(context, isbn, aisle):
    context.header = {'Content-Type': 'application/json;charset=UTF-8'}
    context.add_book_url = get_config()['API']['endpoint'] + ApiResourses.add_book
    context.js_payload = add_book_payload(isbn, aisle)


# GitHub Authentication Verification
@given('I have GitHub auth credentials')
def step_impl(context):
    context.se = requests.session()
    context.se.auth = auth = (get_username(), get_password())


@when('I hit get access API to GitHub')
def step_impl(context):
    context.response = context.se.get(ApiResourses.github_url, auth=context.se.auth)


@then('status code of response should be {status_code:d}')
def step_impl(context, status_code):
    print(context.response.status_code)
    assert context.response.status_code == status_code
