# Generated by Django 2.0 on 2019-10-21 21:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20191021_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 21, 21, 15, 32, 905164), verbose_name='添加时间'),
        ),
    ]