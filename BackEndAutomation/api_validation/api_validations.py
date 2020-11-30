import json
import requests


response = requests.get('http://216.10.245.166//Library/GetBook.php', params={'AuthorName': 'FirstName LastName'}, )
print(type(response))
# John TEst Author
print(response.text)
print(type(response.text))
dict_response = json.loads(response.text)
print(dict_response)
print(type(dict_response))
print(dict_response[0]['isbn'])
json_response = response.json()
print(type(json_response))
print(len(json_response))
print(json_response)
print(json_response[0]['isbn'])
print(response.status_code)
assert response.status_code == 200
print(response.headers)
assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'
print(" ")

# Retrieve the book details with ISBN KLMN
for actual_book in json_response:
    if actual_book['isbn'] == 'Gaurav':
        print(actual_book)
        break


expected_book = {
        "book_name": "Learn API Automation from Excel",
        "isbn": "Gaurav",
        "aisle": "1544"
    }

print(actual_book)
print(expected_book)
assert actual_book == expected_book