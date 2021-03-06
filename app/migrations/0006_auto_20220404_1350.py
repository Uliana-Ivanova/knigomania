# Generated by Django 2.2.27 on 2022-04-04 10:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20220404_1303'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='auther',
            new_name='author',
        ),
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2022, 4, 4, 13, 49, 21, 408840), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2022, 4, 4, 13, 49, 21, 409839), verbose_name='Дата комментария'),
        ),
    ]
