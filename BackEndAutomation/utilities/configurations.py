import configparser
import mysql.connector
import random
import string
from mysql.connector import Error


def get_config():
    config = configparser.ConfigParser()
    config.read('/Users/PycharmProjects/BackEndAutomation/utilities/properties.ini')
    return config


def get_username():
    return 'VitalR'


def get_password():
    return 'password1234'


# connection = mysql.connector.connect(host='localhost', database='APIDevelop', user='root', password='mysql1234')

connect_config = {
    'host': get_config()['SQL']['host'],
    'database': get_config()['SQL']['database'],
    'user': get_config()['SQL']['user'],
    'password': get_config()['SQL']['password'],
}


def get_connection():
    try:
        connection = mysql.connector.connect(**connect_config)
        if connection.is_connected():
            print('Connection Successfull')
            return connection
    except Error as e:
        print(e)


def get_query(query):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    connection.close()
    return row


def get_rand_str():
    letters = string.ascii_lowercase
    isbn_rand = ''.join(random.choice(letters) for i in range(7))
    return isbn_rand


def get_rand_num():
    aisle_rand = random.randrange(1000)
    return aisle_rand
