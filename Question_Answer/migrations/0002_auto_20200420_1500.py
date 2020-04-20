# Generated by Django 3.0.5 on 2020-04-20 14:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Question_Answer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='question_text',
        ),
        migrations.AddField(
            model_name='answer',
            name='Answer_text',
            field=models.TextField(default=django.utils.timezone.now, max_length=50000, unique=True),
            preserve_default=False,
        ),
    ]
