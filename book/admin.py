from django.contrib import admin

# Register your models here.
from book.models import *

admin.site.register(Book)
admin.site.register(BookType)
admin.site.register(BookImage)
admin.site.register(Author)
admin.site.register(IndexBookImage)
admin.site.register(IndexSaleImage)