import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model
from list_users.serializers import ListUsersSerializer
from match_users.models import Matches
from list_users.models import Coordinate
from rest_framework.test import APIClient, APITestCase

User = get_user_model()


class MatchUsersTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.coordinate = Coordinate.objects.create(longitude='55.19236', latitude='61.297148')

        cls.user_1 = User.objects.create_user(first_name='Иван',
                                              last_name='Иванов',
                                              email='test1@test.test',
                                              sex='мужской',
                                              password='Pass1220',
                                              username='test1'
                                              )

        cls.user_2 = User.objects.create_user(first_name='Алена',
                                              last_name='Иванова',
                                              email='test2@test.test',
                                              sex='женский',
                                              password='Pass1220',
                                              username='test2'
                                              )

    def setUp(self):
        self.client = APIClient()
        self.client.force_authenticate(self.user_2)

    def test_match_user_API_status_code_with_GET(self):
        r = self.client.get(f'/api/clients/{self.user_1.pk}/match')
        self.assertEqual(200, r.status_code)

    def test_match_user_API_data_with_GET(self):
        r = self.client.get(f'/api/clients/{self.user_1.pk}/match')
        equal = User.objects.get(id=self.user_1.pk)
        serializer = ListUsersSerializer(equal)
        self.assertEqual(serializer.data, r.data)

    def test_match_user_API_with_POST_from_user_2(self):
        r = self.client.post(f'/api/clients/{self.user_1.pk}/match', {'like': True})
        self.assertEqual(200, r.status_code)
        self.assertEqual({'like': 'Ваша симпатия доставлена другому участнику'}, r.data)

    def tearDown(self) -> None:
        self.client.logout()

    def setUp(self):
        Matches.objects.create(like_to_user=self.user_1.pk, user=self.user_2)
        self.client = APIClient()
        self.client.force_authenticate(self.user_1)

    def test_match_user_API_with_POST_from_user_1(self):
        r = self.client.post(f'/api/clients/{self.user_2.pk}/match', {'like': True})
        self.assertEqual(200, r.status_code)
        self.assertEqual({'like': 'Вы понравились Алена ! Почта участника: test2@test.test'}, r.data)

    def tearDown(self) -> None:
        self.client.logout()
