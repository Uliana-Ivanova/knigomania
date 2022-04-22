# Generated by Django 2.2.27 on 2022-03-28 08:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique_for_date='posted', verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Краткое содержание')),
                ('content', models.TextField(verbose_name='Полное содержание')),
                ('posted', models.DateTimeField(db_index=True, default=datetime.datetime(2022, 3, 28, 11, 51, 42, 820349), verbose_name='Опубликована')),
            ],
            options={
                'verbose_name': 'Статья блога',
                'verbose_name_plural': 'Статья блога',
                'db_table': 'Posts',
                'ordering': ['-posted'],
            },
        ),
    ]
