# Generated by Django 3.0.5 on 2020-05-31 13:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Question_Answer', '0007_auto_20200528_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='answer',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='Question_Answer.Answer'),
            preserve_default=False,
        ),
    ]
