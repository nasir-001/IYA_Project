# Generated by Django 3.0 on 2021-03-29 19:49

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Helpline_Portal', '0004_auto_20210329_1945'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='Avatar',
        ),
    ]
