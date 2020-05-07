# Generated by Django 2.0 on 2019-10-21 19:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_useraddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 21, 19, 29, 10, 521570), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='icon',
            field=models.ImageField(upload_to='uploads/%Y/%m/%d/', verbose_name='用户头像'),
        ),
    ]