'''
Title:    Lab No. 4 - Get Data from Canvas
Author:   Bruce Elgort
Created:  March 2, 2020

Definitions:

JSON - JavaScript Object Notation
API - Application Programming Interface
pprint - Pretty Print Python Library
SSL - Secure Sockets Layer
HTML - Hypertext Markup Language

'''

import urllib.request
import json
import ssl
import pprint
from html.parser import HTMLParser


class MLStripper(HTMLParser):
    # Do not modify the code in this class
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)


def read_access_key():
    # You will need to write code in this function to retrieve the Canvas access key from the credentials.txt file
    pass
    # The access key should be returned
    pass


def strip_tags(html):
    # Do not modify this code in this function
    s = MLStripper()
    s.feed(html)
    return s.get_data()


def getClasses(api_key, context):
    url = 'https://clarkcollege.instructure.com/api/v1' + \
        '/courses?access_token=' + api_key + '&per_page=1000'
    # What does the line of code below do?
    # Your answer goes here
    response = urllib.request.urlopen(url, context=context)
    # What does the line of code below do?
    # Your answer goes here
    data = response.read()
    data = data.decode("UTF-8")
    # What does the line of code below do?
    # Your answer goes here
    data = json.loads(data)
    print()

    # What does the line of code below do?
    # Your answer goes here
    for i in data:
        # What does the line of code below do?
        # Your answer goes here
        if 'name' in i:
            print(i['name'])


def display_raw_data(data):
    # Experiment with pretty print and describe what it does
    # Your answer goes here
    # Learn more about Pretty Print https://docs.python.org/3/library/pprint.html
    print(pprint.pformat(data, indent=4))


def getAssignments(api_key, context):
    # CTEC 121 course id: 1873038
    url = 'https://clarkcollege.instructure.com/api/v1' + \
        '/courses/1873038/assignments?access_token=' + api_key + '&per_page=1000'
    response = urllib.request.urlopen(url, context=context)
    data = response.read()
    data = data.decode("UTF-8")
    data = json.loads(data)
    print()
    i = 1
    for assignment in data:
        print(f'{i}) {assignment["name"]} due at {assignment["due_at"]}')
        print(80*'-')
        print(strip_tags(assignment['description']))
        i += 1


def get_pages(api_key, context):
    # CTEC 121 course id: 1873038
    url = 'https://clarkcollege.instructure.com/api/v1' + \
        '/courses/1873038/pages?access_token=' + api_key + '&per_page=1000'
    response = urllib.request.urlopen(url, context=context)
    data = response.read()
    data = data.decode("UTF-8")
    data = json.loads(data)
    i = 1
    print()
    for page in data:
        print(f'{i}) {page["title"]}')
        print(60*'-')
        i += 1


def get_my_profile(api_key, context):
    url = 'https://clarkcollege.instructure.com/api/v1' + \
        '/users/self?access_token=' + api_key + '&per_page=1000'
    response = urllib.request.urlopen(url, context=context)
    data = response.read()
    data = data.decode("UTF-8")
    data = json.loads(data)
    print()
    for key, value in data.items():
        # What does the line of code below do?
        # Your answer goes here
        if isinstance(value, dict):
            # What does the line of code below do?
            # Your answer goes here
            for k, v in value.items():
                print(f"{k.upper()}: {v}")
        else:
            print(f'{key.upper()}: {value}')


def main():
    # allows us not worry about SSL verification
    context = ssl._create_unverified_context()
    api_key = read_access_key()

    options = ['\n\nAvailable Options\n', 30 * '=', '\n1) Display My Classes\n', '2) Display My Assignments\n', '3) Display List of Content Pages\n',
               '4) Get My Canvas Profile Info\n\n', 'Please make a selection (enter any other number of letter to quit):\n']

    while True:
        # What does the line of code below do?
        # Your answer goes here
        option = int(input(''.join(options)))
        if option == 1:
            getClasses(api_key, context)  # get list of classes
        elif option == 2:
            getAssignments(api_key, context)  # get list of assignments
        elif option == 3:
            get_pages(api_key, context)  # get list of pages from Canvas
        elif option == 4:
            get_my_profile(api_key, context)  # get Canvas profile info
        else:
            break  # get out of the while loop


main()
