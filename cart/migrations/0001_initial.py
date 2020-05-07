# Generated by Django 2.0 on 2019-10-23 18:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0003_book_unit'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False)),
                ('number', models.IntegerField(verbose_name='商品数量')),
                ('tatal', models.DecimalField(decimal_places=2, max_digits=6, null=True, verbose_name='商品总价')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Book', verbose_name='书籍名称')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='所属用户')),
            ],
            options={
                'verbose_name': '购物车',
                'verbose_name_plural': '购物车',
                'db_table': 'cart',
            },
        ),
    ]