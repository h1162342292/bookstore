# Generated by Django 2.0 on 2019-10-25 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_historybook'),
    ]

    operations = [
        migrations.AddField(
            model_name='historybook',
            name='number',
            field=models.IntegerField(default=0, verbose_name='浏览次数'),
        ),
    ]