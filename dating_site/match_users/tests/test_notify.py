import os
from django.test import SimpleTestCase
from match_users.services.notify import Notify
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()


class NotifyServiceTest(SimpleTestCase):

    def setUp(self) -> None:
        # данные для емайл
        self.email = ["test@test.test"]
        self.subject = "Вам выразили симпатию"
        self.message = f'Вы понравились Маше Ивановой! Почта участника: test@test.test'

    def test_send_email(self):
        self.assertEqual(1, Notify().send_email(emails=self.email,
                                                subject=self.subject,
                                                message=self.message,
                                                ))
