from pprint import pprint

from rest_framework.test import APIClient, APITestCase

# Create your tests here.
from .models import Number


class NumberAndMessageTest(APITestCase):
    def setUp(self):
        super().setUp()
        self.dummy_msg = 101010101010

        self.number = self.client.post('/create').json().get('number')

    def test_create_number(self):
        response = self.client.post('/create').json()
        first_number = response.get('number')
        second_number = Number.objects.get(number=first_number).number
        print(first_number, self.number)

        self.assertEqual(first_number, second_number)

    def test_get_message_list(self):
        self.client.post('/send', data={
            'msg': self.dummy_msg,
            'number': self.number
        })
        response = self.client.get('/list/{}'.format(self.number)).json()
        # pprint(response)
        self.assertEqual(response[0].get('msg'), self.dummy_msg)

    def test_send_message(self):
        response = self.client.post('/send', data={
            'msg': self.dummy_msg,
            'number': self.number
        }).json()
        # pprint(response)
        self.assertEqual(response.get('msg'), self.dummy_msg)

    def test_new_message(self):
        self.client.post('/send', data={
            'msg': self.dummy_msg,
            'number': self.number
        })
        self.client.post('/send', data={
            'msg': self.dummy_msg,
            'number': self.number
        })

        response = self.client.get('/list/{}'.format(self.number)).json()
        self.assertEqual(len(response), 2)
        self.client.post('/send', data={
            'msg': self.dummy_msg,
            'number': self.number
        })
        response = self.client.get('/list/{}/new'.format(self.number)).json()
        self.assertEqual(len(response), 1)
