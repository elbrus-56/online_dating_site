from django.contrib import admin

from list_users.models import Coordinate


@admin.register(Coordinate)
class UserAdmin(admin.ModelAdmin):
    pass
