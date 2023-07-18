from django.core.files.base import ContentFile
from django_filters.compat import TestCase
from register_user.serializers import CreateUserSerializer, LoginSerializer


class TestSerializers(TestCase):
    def setUp(self):
        self.data = {}
        with open('register_user/tests/data/1478026379.jpg', mode='rb') as fp:
            self.document = ContentFile(fp.read(), '1478026379.jpg')

        self.payload = {"first_name": "Иван",
                        "last_name": "Иванов",
                        "email": "ivan_ivanov@test.test",
                        "sex": "мужской",
                        "password": "1220Qwer",
                        "asas": 12212121,
                        "photo": self.document}

    def test_CreateUserSerializer(self):
        serializer = CreateUserSerializer(data=self.payload)
        serializer.is_valid(raise_exception=True)
        expected_data = {"first_name": "Иван",
                         "last_name": "Иванов",
                         "email": "ivan_ivanov@test.test",
                         "sex": "мужской",
                         "password": "1220Qwer",
                         "photo": self.document}

        self.assertEqual(expected_data, serializer.validated_data)

    def test_LoginSerializer(self):
        serializer = LoginSerializer(data=self.payload)
        serializer.is_valid(raise_exception=True)
        expected_data = {
            "email": "ivan_ivanov@test.test",
            "password": "1220Qwer",
        }
        self.assertEqual(expected_data, serializer.validated_data)
