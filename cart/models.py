from django.db import models

# Create your models here.
from book.models import Book, BookBase
from user.models import UserProfile


class Cart(BookBase):
    book = models.ForeignKey(to=Book,on_delete=models.CASCADE,verbose_name='书籍名称')
    user = models.ForeignKey(to=UserProfile,on_delete=models.CASCADE,verbose_name='所属用户')
    number = models.IntegerField(verbose_name='商品数量')
    total = models.DecimalField(max_digits=6,decimal_places=2,verbose_name='商品总价',null=True)

    class Meta:
        db_table = 'cart'
        verbose_name = '购物车'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.user.username