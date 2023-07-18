from django.contrib import admin
from match_users.models import Matches


@admin.register(Matches)
class MathesUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'like_to_user')
