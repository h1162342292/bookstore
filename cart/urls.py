from django.urls import path

from cart.views import add_cart, show_cart, delete_cart, add_num

app_name = 'cart'
urlpatterns = [
    path('add',add_cart,name='add'),
    path('show',show_cart,name='show'),
    path('delete',delete_cart,name='delete'),
    path('add_num',add_num,name='add_num')
]