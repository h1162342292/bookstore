# Generated by Django 2.0 on 2019-10-24 19:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_auto_20191023_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 24, 19, 3, 40, 832839), verbose_name='添加时间'),
        ),
    ]