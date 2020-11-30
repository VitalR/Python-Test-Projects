import random
import requests
import string
import configparser
from payload import *
from utilities.configurations import *
from utilities.resourses import *

# input_payload = {
#     "name": "104 Learn Appium Test Automation with Python",
#     "isbn": "bcdtest",
#     "aisle": "2280",
#     "author": "John TEst Author"
# }

config = configparser.ConfigParser()
config.read('/Users/PycharmProjects/BackEndAutomation/utilities/properties.ini')

letters = string.ascii_lowercase
isbn_rand = ''.join(random.choice(letters) for i in range(7))

# add_book_response = requests.post('http://216.10.245.166/Library/Addbook.php', json=add_book_payload(isbn_rand), headers=header)
# add_book_response = requests.post(config['API']['endpoint'] + '/Library/Addbook.php', json=add_book_payload(isbn_rand),
#                                   headers=header)

# Add Book
header = {'Content-Type': 'application/json;charset=UTF-8'}
config = get_config()
add_book_url = config['API']['endpoint'] + ApiResourses.add_book
query = 'select * from Books'
add_book_response = requests.post(add_book_url, json=build_payload_from_db(query),
                                  headers=header)
# add_book_response = requests.post(add_book_url, json=add_book_payload(isbn_rand),
#                                   headers=header)
print(add_book_response.json())
response_dict = add_book_response.json()
assert add_book_response.status_code == 200
assert response_dict['Msg'] == 'successfully added'

# {'Msg': 'successfully added', 'ID': 'bcdtest2279'}
book_id = response_dict['ID']

# Delete Book
header_del = {'ID': book_id}
delete_book_url = config['API']['endpoint'] + ApiResourses.delete_book
delete_book_response = requests.post(delete_book_url, json=header_del, headers=header)
response_dict_delete = delete_book_response.json()

print(delete_book_response.status_code)
assert delete_book_response.status_code == 200
print(response_dict_delete['msg'])
assert response_dict_delete['msg'] == 'book is successfully deleted'


# Post a Multipart-Encoded File
url = 'https://httpbin.org/post'
files = {'file': open('/Users/PycharmProjects/BackEndAutomation/utilities/properties.ini', 'rb')}

r = requests.post(url, files=files)
print(r.text)
# print(r.content)
# print(r.status_code)
# print(r.headers)
# print(r.cookies)


# Base Authentication
se = requests.session()
se.auth = auth = ('VitalR', get_password())

url = 'https://api.github.com/user'
response = requests.get(url, auth=('VitalR', get_password()))
print(response.status_code)
# print(response.content)
# print(response.text)
response_msg = response.json()
print(response_msg['message'])
print(' ')

url2 = 'https://api.github.com/user/repos'
response = se.get(url2)
print(response.status_code)
