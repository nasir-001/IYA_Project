# Generated by Django 3.0.4 on 2020-03-28 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Helpline_Portal', '0006_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='id',
        ),
        migrations.RemoveField(
            model_name='users',
            name='id',
        ),
        migrations.AlterField(
            model_name='staff',
            name='regnumber',
            field=models.CharField(max_length=11, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='users',
            name='regnumber',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]