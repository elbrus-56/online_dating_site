from django.db import models

from register_user.models import User


class Matches(models.Model):
    like_to_user = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True, related_name='likes')

    class Meta:
        db_table = 'dating_site_matches'
        verbose_name = 'Совпадение'
        verbose_name_plural = 'Совпадения'

    def __str__(self):
        return f'ID: {self.id} : {self.user.first_name} {self.user.last_name} :' \
               f' поставила like пользователю ID : {self.like_to_user}'
