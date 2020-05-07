# Generated by Django 2.0 on 2019-10-24 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_book_unit'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderBooks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False)),
                ('number', models.IntegerField(default=1, verbose_name='书籍数量')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='书籍单价')),
                ('comment', models.CharField(max_length=256, verbose_name='书籍评论')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Book')),
            ],
            options={
                'verbose_name': '订单书籍表',
                'verbose_name_plural': '订单书籍表',
                'db_table': 'order_books',
            },
        ),
        migrations.RemoveField(
            model_name='ordergoods',
            name='goods',
        ),
        migrations.RemoveField(
            model_name='ordergoods',
            name='order',
        ),
        migrations.RemoveField(
            model_name='order',
            name='goods_number',
        ),
        migrations.RemoveField(
            model_name='order',
            name='goods_total',
        ),
        migrations.AddField(
            model_name='order',
            name='books_number',
            field=models.IntegerField(default=0, verbose_name='书籍总量'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='books_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='书籍总价'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='OrderGoods',
        ),
        migrations.AddField(
            model_name='orderbooks',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Order'),
        ),
    ]
