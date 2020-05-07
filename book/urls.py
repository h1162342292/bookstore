from django.urls import path

from book.views import index, book_detail, book_type, search

app_name = 'book'
urlpatterns = [
    path('',index,name='index'),
    path('detail/<int:gid>',book_detail,name='detail'),
    path('type/<int:tid>',book_type,name='type'),
    path('search',search,name='search'),
]