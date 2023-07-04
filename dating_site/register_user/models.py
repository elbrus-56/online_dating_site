from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    SEX = [
        ('мужской', 'Мужской'),
        ('женский', 'Женский')

    ]
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    sex = models.TextField(choices=SEX, verbose_name='Пол', blank=True)
    photo = models.ImageField(upload_to='images/%Y-%m-%d/', default='images/default.png',
                              max_length=200, verbose_name='Фото')
    username = models.CharField(max_length=150, blank=True)

    class Meta:
        db_table = 'dating_site_user'
        verbose_name = 'Посетитель'
        verbose_name_plural = 'Посетители'
        ordering = ['id']
