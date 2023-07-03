from django.contrib import admin
from register_user.models import User


@admin.register(User)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'sex', 'photo')
