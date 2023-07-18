from django.urls import reverse
from list_users.models import Coordinate
from register_user.models import User
from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class ListUsersTest(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.url = reverse('list_users')

        self.coordinate_1 = Coordinate.objects.create(longitude='55.188910', latitude='61.332720')  # Члб
        self.coordinate_2 = Coordinate.objects.create(longitude='55.182517', latitude='61.292831')  # Члб 2
        self.coordinate_3 = Coordinate.objects.create(longitude='55.710801', latitude='37.607318')  # Мск
        self.coordinate_4 = Coordinate.objects.create(longitude='55.710901', latitude='37.107318')  # Мск 2

        self.user = User.objects.create_user(first_name='Иван',
                                             last_name='Иванов',
                                             email='test1@test.test',
                                             sex='мужской',
                                             password='Pass1220',
                                             username='test1',
                                             )
        self.user.coordinate.add(self.coordinate_1)

        self.user2 = User.objects.create_user(first_name='Марина',
                                              last_name='Петрова',
                                              email='test2@test.test',
                                              sex='женский',
                                              password='Pass1220',
                                              username='test2',
                                              )
        self.user2.coordinate.add(self.coordinate_2)

        self.user3 = User.objects.create_user(first_name='Елена',
                                              last_name='Петрова',
                                              email='test3@test.test',
                                              sex='женский',
                                              password='Pass1220',
                                              username='test3',
                                              )
        self.user3.coordinate.add(self.coordinate_3)

        self.user4 = User.objects.create_user(first_name='Игорь',
                                              last_name='Иванов',
                                              email='test4@test.test',
                                              sex='мужской',
                                              password='Pass1220',
                                              username='test4',
                                              )
        self.user4.coordinate.add(self.coordinate_4)

        self.client.force_authenticate(self.user)

    def test_list_users_api(self):
        r = self.client.get(self.url)
        self.assertEqual(status.HTTP_200_OK, r.status_code)
        users = User.objects.all()
        self.assertEqual(len(users), len(r.data))

    def test_filter_by_sex(self):
        r = self.client.get(self.url, data={'sex': 'мужской'})
        self.assertEqual(2, len(r.data))

        r = self.client.get(self.url, data={'sex': 'женский'})
        self.assertEqual(2, len(r.data))

    def test_filter_by_first_name(self):
        r = self.client.get(self.url, data={'first_name': 'Иван'})
        self.assertEqual(1, len(r.data))

    def test_filter_by_last_name(self):
        r = self.client.get(self.url, data={'last_name': 'Петрова'})
        self.assertEqual(2, len(r.data))

    def test_filter_by_distance(self):
        r = self.client.get(self.url, data={'distance': 5})
        self.assertEqual(1, len(r.data))

        r = self.client.get(self.url, data={'distance': 5000})
        self.assertEqual(3, len(r.data))

        r = self.client.get(self.url, data={'distance': 1})
        self.assertEqual(0, len(r.data))

    def test_some_filters(self):
        r = self.client.get(self.url, data={'sex': 'женский', 'distance': 500})
        print(r.data)
