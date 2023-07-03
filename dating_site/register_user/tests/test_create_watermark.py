import os
from unittest import mock
from django.test import TestCase, SimpleTestCase
# from unittest import TestCase
import random
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from register_user.services.create_watermark import Watermark


class WatermarkTest(SimpleTestCase):

    def setUp(self) -> None:
        self.img = '../tests/data/1478026379.jpg'
        self.output = '../tests/data/1478026379_watermark.jpg'

    def test_create_watermark(self):
        """
        Функция создает watermark на изображении.
        """
        Watermark().create_watermark(self.img, self.output)




