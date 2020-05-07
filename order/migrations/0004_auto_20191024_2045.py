# Generated by Django 2.0 on 2019-10-24 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20191024_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='订单总价'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='carriage_price',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=6, verbose_name='运费'),
        ),
    ]