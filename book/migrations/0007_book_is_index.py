# Generated by Django 2.0 on 2019-10-27 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_auto_20191025_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_index',
            field=models.BooleanField(default=False, verbose_name='是否首页展示'),
        ),
    ]
