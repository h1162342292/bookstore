# Generated by Django 2.0 on 2019-10-23 19:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20191023_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 23, 19, 7, 21, 441297), verbose_name='添加时间'),
        ),
    ]
