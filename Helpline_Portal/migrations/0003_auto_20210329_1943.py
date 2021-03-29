# Generated by Django 3.0 on 2021-03-29 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Helpline_Portal', '0002_auto_20210329_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_student',
            field=models.BooleanField(default=False, verbose_name='student status'),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_teacher',
            field=models.BooleanField(default=False, verbose_name='teacher status'),
        ),
    ]
