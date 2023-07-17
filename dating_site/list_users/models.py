from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Coordinate(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                             related_name='coordinate')

    class Meta:
        db_table = 'dating_site_coordinate'
        verbose_name = 'Местоположение пользователя'
        verbose_name_plural = 'Местоположение пользователей'

    def __str__(self):
        return f'ID: {self.pk} : ({self.longitude}, {self.latitude})'
