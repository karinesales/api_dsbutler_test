import json
import unittest
import requests

from projects_tests.json_scenarios.utils import *


class GetProjectTest(unittest.TestCase):

    def setUp(self):
        self.url = baseUrl()

    #Envio do body com atributos esperados
    def test_getProjectWithSucess(self):
        #arrange
        folder = createProjectTest(self)

        #act
        response = requests.get(f'{self.url}/projects?title={folder}')

        #asserts
        self.assertEqual(response.status_code, 200)
        json_data = json.loads(response.text)
        self.assertIn('title', json_data)
        self.assertEqual(type(json_data['title']), str)
        if 'description' in json_data:
            self.assertEqual(type(json_data['description']), str)
        itemAuthors = json_data['authors']

        for authors in itemAuthors:
            self.assertEqual(type(authors), str)

        self.assertIn('license', json_data)
        self.assertEqual(type(json_data['license']), str)

        self.assertIn('folder', json_data)
        self.assertEqual(type(json_data['folder']), str)

        if 'repository' in json_data:
            self.assertEqual(type(json_data['repository']), str)

        self.assertIn('ignored', json_data)
        if len(json_data['ignored']) != 0:
            for itemIg in json_data['ignored']:
                self.assertEqual(type(itemIg), str)

    # Envio de atributo inexistente
    def test_createProjectNullTitleBody(self):
            # arrange
            folder = 'project_inexistent'
            # act
            response = requests.get(f'{self.url}/projects?title={folder}')

            # asserts
            self.assertEqual(response.status_code, 404)

            #Mensagem não amigável identificando o problema ocorrido, status code 500.




