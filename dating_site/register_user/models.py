import datetime
import os
import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


def get_random_filename(instance, filename) -> str:
    """
    Функция генерирует имя для изображения
    """
    extension = filename.split('.')[-1]
    filename = f'{str(uuid.uuid4())}.{extension}'
    return os.path.join(f'images/{datetime.datetime.now().strftime("%d-%m-%Y")}/',
                        filename)


class User(AbstractUser):

    SEX = [
        ('мужской', 'Мужской'),
        ('женский', 'Женский')

    ]

    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    sex = models.TextField(choices=SEX, verbose_name='Пол', blank=True)
    photo = models.ImageField(
        upload_to=get_random_filename,
        default='images/default.png',
        max_length=200,
        verbose_name='Фото')
    username = models.CharField(max_length=150, blank=True)

    class Meta:
        db_table = 'dating_site_user'
        verbose_name = 'Посетитель'
        verbose_name_plural = 'Посетители'
        ordering = ['id']

    def __str__(self):
        return f'Пользователь: {self.email}'
