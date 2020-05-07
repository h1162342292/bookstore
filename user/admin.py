from django.contrib import admin

# Register your models here.
from user.models import UserProfile, UserAddress

admin.site.register(UserProfile)
admin.site.register(UserAddress)
admin.site.site_header = '三岁书屋后台管理'
admin.site.site_title = '三岁书屋'