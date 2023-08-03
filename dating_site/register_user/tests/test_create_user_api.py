from django.core.files.base import ContentFile
from register_user.models import User
from rest_framework.test import APIClient, APITestCase


class CreateOrdersViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.data = {}
        with open('register_user/tests/data/1478026379.jpg', mode='rb') as fp:
            document = ContentFile(fp.read(), '1478026379.jpg')

        self.data['first_name'] = 'Иван',
        self.data['last_name'] = 'Иванов',
        self.data['email'] = 'ivan_ivanov@test.test',
        self.data['sex'] = 'мужской',
        self.data['password'] = '1220Qwer',
        self.data['photo'] = document

        self.data_2 = {}
        self.data_2['first_name'] = 'Sergey',
        self.data_2['last_name'] = 'Иванов',
        self.data_2['email'] = 'sergey_ivanov@test.test',
        self.data_2['sex'] = 'мужской',
        self.data_2['password'] = '1220Qwer',

    def test_register_user_api_with_image(self):
        r = self.client.post(
            path='/api/clients/create/',
            data=self.data
        )
        user = User.objects.filter(email='ivan_ivanov@test.test').exists()

        self.assertEqual(201, r.status_code)
        self.assertTrue(user)

    def test_register_user_api_without_image(self):
        r = self.client.post(
            path='/api/clients/create/',
            data=self.data_2
        )
        user = User.objects.filter(email='sergey_ivanov@test.test').exists()

        self.assertEqual(201, r.status_code)
        self.assertTrue(user)
