from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class UserProfile(AbstractUser):
    phone = models.CharField(max_length=11,unique=True,verbose_name='手机号码')
    icon = models.ImageField(upload_to='uploads/%Y/%m/%d/',verbose_name='用户头像')
    class Meta:
        db_table = 'userprofile'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name

class UserAddress(models.Model):
    receiver = models.CharField(max_length=20,verbose_name='收件人')
    address = models.CharField(max_length=256,verbose_name='收货地址')
    code = models.CharField(max_length=6,verbose_name='邮政编码')
    phone = models.CharField(max_length=11,verbose_name='联系电话')
    is_default = models.BooleanField(default=False,verbose_name='是否为默认地址')
    add_time = models.DateTimeField(default=datetime.now(),verbose_name='添加时间')
    user = models.ForeignKey(to=UserProfile,on_delete=models.CASCADE,verbose_name='所属用户')

    class Meta:
        db_table ='address'
        verbose_name = '地址表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.address

