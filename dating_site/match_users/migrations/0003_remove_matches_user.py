# Generated by Django 4.2.2 on 2023-07-05 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('match_users', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matches',
            name='user',
        ),
    ]