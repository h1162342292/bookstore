# Generated by Django 2.0 on 2019-10-25 21:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_auto_20191025_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 25, 21, 22, 38, 152768), verbose_name='添加时间'),
        ),
    ]
