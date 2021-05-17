import requests
from faker import Faker


def createTitle():
    fake = Faker()
    title = fake.name()
    return title

def baseUrl():
    baseUrl = "http://127.0.0.1:5000/dsb-api"
    return baseUrl


def bodyCreateProject():
    data = {
        "title": createTitle(),
        "description": "A description test",
        "authors": [
            "A1 <a1@email.com>"
        ],
        "license": "MIT",
        "repository": "",
        "ignored": [
            "data, model"
        ]
    }
    return data

def bodyWithoutTitle():
    data = {
        "description": "A description test",
        "authors": [
            "A1 <a1@email.com>"
        ],
        "license": "MIT",
        "repository": "",
        "ignored": [
            "data, model"
        ]
    }
    return data

def createProjectTest(self):
    body = {
        "title": "Test Test",
        "description": "A description test",
        "authors": [
            "A1 <a1@email.com>"
        ],
        "license": "MIT",
        "repository": "",
        "ignored": [
            "data, model"
        ]
    }
    requests.post(f'{self.url}/projects', json=body)
    return "test_test"

