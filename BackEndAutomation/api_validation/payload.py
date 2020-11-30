from utilities.configurations import *


def add_book_payload(isbn, aisle):
    body = {
        "name": "104 Learn Appium Test Automation with Python",
        "isbn": isbn,
        "aisle": aisle,
        "author": "John TEst Author"
    }
    return body


def build_payload_from_db(query):
    add_body = {}
    tp = get_query(query)
    add_body['name'] = tp[0]
    add_body['isbn'] = tp[1]
    add_body['aisle'] = tp[2]
    add_body['author'] = tp[3]
    return add_body
