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

    def test_register_user_api(self):
        r = self.client.post(
            path='/api/clients/create/',
            data=self.data
        )
        user = User.objects.all()
        self.assertEqual(201, r.status_code)
        self.assertEqual(1, len(user))
