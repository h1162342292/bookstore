# Generated by Django 2.0 on 2019-10-22 20:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20191021_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 22, 20, 39, 3, 323477), verbose_name='添加时间'),
        ),
    ]