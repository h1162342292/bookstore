# Generated by Django 2.0 on 2019-10-25 21:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_auto_20191024_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 25, 21, 6, 39, 950366), verbose_name='添加时间'),
        ),
    ]