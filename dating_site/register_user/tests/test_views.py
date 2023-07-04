import os

from django.core.files.base import ContentFile
from django.test import TestCase
# from unittest import TestCase
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()


class CreateOrdersViewTest(TestCase):
    def setUp(self):
        self.data = {}
        with open('register_user/tests/data/1478026379.jpg', mode='rb') as fp:
            document = ContentFile(fp.read(), '1478026379.jpg')

        self.data['first_name'] = 'Иван',
        self.data['last_name'] = 'Иванов',
        self.data['email'] = 'ivan_ivanov@test.test',
        self.data['sex'] = 'мужской',
        self.data['password'] = '1220Qwer',
        self.data['photo'] = document

    def test_register_user_API(self):
        r = self.client.post(
            path='/api/clients/create/',
            data=self.data
        )
        print(r.data)
        self.assertEqual(201, r.status_code)
