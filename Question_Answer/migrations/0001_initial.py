<<<<<<< HEAD
# Generated by Django 3.0.6 on 2020-06-02 12:29
=======
# Generated by Django 3.0.5 on 2020-05-31 13:42
>>>>>>> d999ee1f1e4a9bfd794debd8d578bb3b75a6b3ae

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.TextField(max_length=50000, unique=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('liked', models.ManyToManyField(blank=True, default=None, related_name='answer_liked', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True)),
                ('slug', models.SlugField(editable=False, max_length=150, unique=True)),
                ('description', models.CharField(max_length=300)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_title', models.CharField(max_length=150, unique=True)),
                ('question_text', models.TextField(max_length=50000, unique=True)),
                ('slug', models.SlugField(editable=False, max_length=150, unique=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Question_Answer.Category')),
                ('liked', models.ManyToManyField(blank=True, default=None, related_name='question_liked', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-pub_date'],
                'get_latest_by': '-pk',
            },
        ),
        migrations.CreateModel(
<<<<<<< HEAD
            name='QuestionLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], default='Like', max_length=10)),
=======
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], default='Like', max_length=10)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Question_Answer.Question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.TextField(max_length=50000, unique=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('liked', models.ManyToManyField(blank=True, default=None, related_name='answer_liked', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
>>>>>>> d999ee1f1e4a9bfd794debd8d578bb3b75a6b3ae
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Question_Answer.Question')),
            ],
        ),
        migrations.CreateModel(
            name='AnswerLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], default='Like', max_length=10)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Question_Answer.Answer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Question_Answer.Question'),
        ),
    ]
