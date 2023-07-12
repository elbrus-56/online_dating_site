import django
import os

from rest_framework import status
from rest_framework.exceptions import ErrorDetail
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient

from list_users.serializers import ListUsersSerializer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from register_user.models import User


class LoginTest(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_user(first_name='Иван',
                                             last_name='Иванов',
                                             email='test1@test.test',
                                             sex='мужской',
                                             password='Pass1220',
                                             username='test1'
                                             )

    def test_login_api_with_not_login(self):
        self.assertTrue(self.user.is_authenticated)

        r = self.client.get(reverse('list_users'))

        self.assertEqual(status.HTTP_403_FORBIDDEN, r.status_code)
        self.assertEqual({'detail': ErrorDetail(string='Учетные данные не были предоставлены.',
                                                code='not_authenticated')}, r.data)

    def test_login_api_with_login(self):
        r = self.client.post(reverse('login_user'), data={'email': 'test1@test.test', 'password': 'Pass1220'})
        self.assertEqual(status.HTTP_200_OK, r.status_code)
        self.assertEqual({'login': 'Аутентификация прошла успешно'}, r.data)

        r = self.client.get(reverse('list_users'))
        self.assertEqual(status.HTTP_200_OK, r.status_code)
        #
        # serializer = ListUsersSerializer(self.user)
        # print(serializer.data)
        # print(r.data)
        #
        # self.assertEqual(serializer.data, r.data)
