from django.urls import path

from order.views import generate_order, order_commit, order_pay, check_order, order_comment

app_name = 'order'
urlpatterns = [
    path('generate', generate_order, name='generate'),
    path('commit', order_commit, name='commit'),
    path('pay', order_pay, name='pay'),
    path('check', check_order, name='check'),
    path('comment',order_comment,name='comment')
]