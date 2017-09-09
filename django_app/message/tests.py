from rest_framework.test import APIClient, APITestCase

# Create your tests here.
from .models import Number


class NumberAndMessageTest(APITestCase):
    def setUp(self):
        super().setUp()

        self.number = self.client.get('/create').json().get('number')

    def test_create_number(self):
        response = self.client.get('/create').json()
        first_number = response.get('number')
        second_number = Number.objects.get(number=first_number).number

        self.assertEqual(first_number, second_number)

    def test_get_message_list(self):
        # response = self.client.get('/list/{}'.format(self.number))
        pass

    def test_send_message(self):
        pass
