import base64
import os

from django.test import TestCase
# from unittest import TestCase
import django



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from list_users.serializers import ListUsersSerializer
from match_users.models import Matches
from list_users.models import Coordinate

User = get_user_model()


class MatchUsersTest(TestCase):

    def setUp(self):
        self.password = make_password('Pass1220')
        coordinate = Coordinate.objects.create(longitude='55.19236', latitude='61.297148')

        self.user_1 = User.objects.create(first_name='Иван',
                                          last_name='Иванов',
                                          email='test@test.test',
                                          sex='мужской',
                                          password=self.password
                                          )

        self.user_2 = User.objects.create(first_name='Алена',
                                          last_name='Иванова',
                                          email='test1@test.test',
                                          sex='женский',
                                          password=self.password
                                          )

        self.headers = {
            'HTTP_AUTHORIZATION': 'Basic ' +
                                  base64.b64encode(b'test1@test.test:Pass1220').decode("utf-8")
        }

    def test_match_user_API_status_code_GET(self):
        r = self.client.get(f'/api/clients/{self.user_1.pk}/match', **self.headers)
        self.assertEqual(200, r.status_code)

    def test_match_user_API_data_GET(self):
        r = self.client.get(f'/api/clients/{self.user_1.pk}/match', **self.headers)
        equal = User.objects.get(id=self.user_1.pk)
        serializer = ListUsersSerializer(equal)
        self.assertEqual(serializer.data, r.data)

    def test_match_user_API_status_code_POST(self):
        r = self.client.post(f'/api/clients/{self.user_1.pk}/match', {'like': True}, **self.headers)
        self.assertEqual(200, r.status_code)


class MatchUsers2Test(TestCase):

    def setUp(self):
        self.password = make_password('Pass1220')

        coordinate = Coordinate.objects.create(longitude='55.19236', latitude='61.297148')

        self.user_1 = User.objects.create(first_name='Иван',
                                          last_name='Иванов',
                                          email='test1@test.test',
                                          sex='мужской',
                                          password=self.password
                                          )

        self.user_2 = User.objects.create(first_name='Алена',
                                          last_name='Иванова',
                                          email='test2@test.test',
                                          sex='женский',
                                          password=self.password
                                          )
        Matches.objects.create(like_to_user=self.user_2.pk, user=self.user_1)

        self.headers = {
            'HTTP_AUTHORIZATION': 'Basic ' +
                                  base64.b64encode(b'test2@test.test:Pass1220').decode("utf-8")
        }

    def test_match_user_API_status_code_POST(self):
        r = self.client.post(f'/api/clients/{self.user_1.pk}/match', {'like': True}, **self.headers)
        print(r.data)
        self.assertEqual(200, r.status_code)
