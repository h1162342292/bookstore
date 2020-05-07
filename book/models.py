from django.db import models

# Create your models here.
from user.models import UserProfile


class BookBase(models.Model):
    add_time = models.DateTimeField(auto_now_add=True,verbose_name='添加时间')
    update_time = models.DateTimeField(auto_now_add=True,verbose_name='更新时间')
    is_delete = models.BooleanField(default=False)
    class Meta:
        abstract = True
class BookType(BookBase):
    name = models.CharField(max_length=10,verbose_name='图书类型')
    image = models.ImageField(upload_to='type',verbose_name='类型图片')
    class Meta:
        db_table = 'book_type'
        verbose_name = '图书类别表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name
class Author(BookBase):
    name = models.CharField(max_length=10,verbose_name='笔名',unique=True)
    country = models.CharField(max_length=10,verbose_name='国籍')
    class Meta:
        db_table = 'author'
        verbose_name = '作家表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name
class Book(BookBase):
    name = models.CharField(max_length=20,verbose_name='书名')
    type = models.ForeignKey(to=BookType,on_delete=models.CASCADE,verbose_name='图书类型')
    inventory = models.IntegerField(default=0,verbose_name='库存量')
    author = models.ForeignKey(to=Author,on_delete=models.CASCADE,verbose_name='作家')
    price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='图书价格')
    image = models.FileField(upload_to='books',verbose_name='图书图片')
    description = models.CharField(max_length=256,verbose_name='图书简介')
    sales = models.IntegerField(default=0,verbose_name='销量')
    details = models.TextField(verbose_name='商品详情')
    status = models.BooleanField(default=True,verbose_name='商品状态')
    unit = models.CharField(max_length=5,default='本')
    is_index = models.BooleanField(default=False,verbose_name='是否首页展示')
    class Meta:
        db_table = 'book'
        verbose_name = '图书表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name
class BookImage(BookBase):
    book = models.ForeignKey(to=Book,on_delete=models.CASCADE,verbose_name='图书')
    image = models.ImageField(upload_to='books',verbose_name='图书路径')

    class Meta:
        db_table = 'book_image'
        verbose_name = '图书图片'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.book.name
class IndexBookImage(BookBase):
    book = models.ForeignKey(to=Book,on_delete=models.CASCADE,verbose_name='图书')
    image = models.ImageField(upload_to='banner',verbose_name='图书图片')
    index = models.IntegerField(default=0,verbose_name='播放顺序')
    class Meta:
        db_table = 'index_book_image'
        verbose_name = '首页轮播图'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.book.name
class IndexSaleImage(BookBase):
    name = models.CharField(max_length=30,verbose_name='促销活动名称')
    image = models.ImageField(upload_to='banner',verbose_name='活动图片')
    index = models.SmallIntegerField(default=0,verbose_name='展示顺序')
    url = models.URLField(verbose_name='活动链接')

    class Meta:
        db_table = 'index_sale'
        verbose_name = '首页促销活动'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name
class HistoryBook(BookBase):
    user = models.ForeignKey(to=UserProfile,on_delete=models.CASCADE,verbose_name='用户')
    book = models.ForeignKey(to=Book,on_delete=models.CASCADE,verbose_name='书籍')
    number = models.IntegerField(verbose_name='浏览次数',default=1)
    class Meta:
        db_table = 'history_book'
        verbose_name = '历史记录'
        verbose_name_plural = verbose_name