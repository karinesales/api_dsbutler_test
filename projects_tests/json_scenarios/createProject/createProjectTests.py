import json
import unittest
import requests

from projects_tests.json_scenarios.utils import *


class CreateProjectTest(unittest.TestCase):

    def setUp(self):
        self.url = baseUrl()

    #Envio do body com atributos esperados
    def test_createProjectWithSucess(self):
        #arrange
        body = bodyCreateProject()

        #act
        response = requests.post(f'{self.url}/projects', json=body)

        #asserts
        self.assertEqual(response.status_code, 201)
        json_data = json.loads(response.text)
        self.assertIn('message', json_data)
        self.assertEqual(type(json_data['message']), str)
        self.assertEqual(json_data['message'], body['title']+" sucessfully created")

    # Envio do body sem atributo mandatório "title"
    def test_createProjectNullTitleBody(self):
            # arrange
            body = bodyWithoutTitle()

            # act
            response = requests.post(f'{self.url}/projects', json=body)

            # asserts
            self.assertEqual(response.status_code, 400)

            #Mensagem não amigável identificando o problema ocorrido

    # Body vazio
    def test_createProjectEmptyBody(self):
        # arrange
        body = {}

        # act
        response = requests.post(f'{self.url}/projects', json=body)

        # asserts
        self.assertEqual(response.status_code, 400)








