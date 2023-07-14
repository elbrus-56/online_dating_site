from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.models import Token

from config.settings import AUTH_USER_MODEL
from list_users.models import Coordinate


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
    coordinate = models.ForeignKey(Coordinate, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='coordinates')

    @receiver(post_save, sender=AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)

    class Meta:
        db_table = 'dating_site_user'
        verbose_name = 'Посетитель'
        verbose_name_plural = 'Посетители'
        ordering = ['id']

    def __str__(self):
        return f'Пользователь: {self.email}'
