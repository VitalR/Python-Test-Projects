import json

courses = '{"name": "SuperMan", "language": ["Java", "Python", "Ruby"]}'

# Loads method parse json string and it returns dictionary
dict_courses = json.loads(courses)
print(type(dict_courses))

print(dict_courses['name'])
print(dict_courses['language'])

# Get the first language taught by trainer
list_languages = dict_courses['language']
print(type(list_languages))
print(list_languages[0])
print(dict_courses['language'][1])


# Parse content present in Json file
with open('courses.json') as f:
    dict_2 = json.load(f)
    print(dict_2['courses'])
    print(dict_2['courses'][1])
    print(dict_2['courses'][1]['title'])

    print(dict_2['dashboard'])
    print(len(dict_2['dashboard']))
    print(dict_2['dashboard']['website'])

# Price of course RPA
    for course in dict_2['courses']:
        print(course)
        if course['title'] == 'RPA':
            print(course['price'])
            assert course['price'] == 45

# Compare two Json Schemas using Python Dictionaries
with open('courses1.json') as fi:
    dict_3 = json.load(fi)
    print(dict_2 == dict_3)
    assert dict_2 == dict_3

