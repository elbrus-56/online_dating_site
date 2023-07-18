import os

import django
from django.test import SimpleTestCase
from register_user.services.watermark import Watermark

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()


class WatermarkTest(SimpleTestCase):

    def setUp(self) -> None:
        self.img = 'register_user/tests/data/1478026379.jpg'
        self.output = 'register_user/tests/data/1478026379_watermark.jpg'

    def test_create_watermark(self):
        """
        Функция создает копию изображения с водяным знаком.
        """
        Watermark().create_watermark(self.img, self.output)
