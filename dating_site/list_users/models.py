from django.db import models


class Coordinate(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()

    class Meta:
        db_table = 'dating_site_coordinate'
        verbose_name = 'Местоположение пользователя'
        verbose_name_plural = 'Местоположение пользователей'

    def __str__(self):
        return f'ID: {self.id} : {self.longitude}, {self.latitude}'
