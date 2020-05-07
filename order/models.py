from django.db import models

# Create your models here.
from book.models import BookBase, Book
from user.models import UserProfile, UserAddress


class Order(BookBase):
    PAY_METHODS = ((1, '微信'), (2, '支付宝'), (3, '银联'), (4, '货到付款'))
    ORDER_STATUS = ((1, '待付款'), (2, '待发货'), (3, '待收货'), (4, '待评价'), (5, '已完成'))
    order_id = models.CharField(max_length=128, primary_key=True, verbose_name='订单编号')
    user = models.ForeignKey(to=UserProfile, on_delete=models.CASCADE, verbose_name='用户')
    address = models.ForeignKey(to=UserAddress, on_delete=models.CASCADE, verbose_name='地址')
    pay_method = models.SmallIntegerField(choices=PAY_METHODS, default=2, verbose_name='支付方式')
    books_number = models.IntegerField(verbose_name='书籍总量')
    books_total = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='书籍总价')
    carriage_price = models.DecimalField(max_digits=6,decimal_places=2,default=10, verbose_name='运费')
    order_status = models.SmallIntegerField(choices=ORDER_STATUS, default=1, verbose_name='订单状态')
    trade_on = models.CharField(max_length=128, verbose_name='支付编号')
    total = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='订单总价')
    class Meta:
        db_table = 'order'
        verbose_name = '订单表'
        verbose_name_plural = verbose_name


class OrderBooks(BookBase):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE)
    books = models.ForeignKey(to=Book, on_delete=models.CASCADE)
    number = models.IntegerField(default=1, verbose_name='书籍数量')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='书籍单价')
    comment = models.CharField(max_length=256, verbose_name='书籍评论')

    class Meta:
        db_table = 'order_books'
        verbose_name = '订单书籍表'
        verbose_name_plural = verbose_name
