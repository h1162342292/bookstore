# Generated by Django 2.0 on 2019-10-27 15:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_auto_20191025_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 27, 15, 16, 55, 514051), verbose_name='添加时间'),
        ),
    ]
