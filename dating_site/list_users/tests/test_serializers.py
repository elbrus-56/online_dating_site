from django.contrib.auth import get_user_model
from django_filters.compat import TestCase
from list_users.serializers import ListUsersSerializer

User = get_user_model()


class TestSerializers(TestCase):
    @classmethod
    def setUpTestData(cls):
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

    def test_list_users_serializer(self):
        serializer = ListUsersSerializer([self.user_1, self.user_2], many=True)
        expected_data = [{'first_name': 'Иван',
                          'last_name': 'Иванов',
                          'sex': 'мужской',
                          'photo': '/media/images/default.png'

                          },
                         {'first_name': 'Алена',
                          'last_name': 'Иванова',
                          'sex': 'женский',
                          'photo': '/media/images/default.png'

                          }
                         ]
        self.assertEqual(expected_data, serializer.data)
