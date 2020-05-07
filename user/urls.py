from django.urls import path

from user.views import index, register, check_user, user_login, user_active, forget_password, send_check, modify_pwd, \
    user_logout, user_center, user_order, user_address, modify_icon

app_name = 'user'
urlpatterns = [
    path('',index,name='index'),
    path('register',register,name='register'),
    path('check_user',check_user,name='check_user'),
    path('login',user_login,name='login'),
    path('active',user_active,name='active'),
    path('forget_pwd',forget_password,name='forget_pwd'),
    path('send',send_check,name='send'),
    path('modify',modify_pwd,name='modify'),
    path('logout',user_logout,name='logout'),
    path('center',user_center,name='center'),
    path('order', user_order, name='order'),
    path('address', user_address, name='address'),
    path('modify_icon',modify_icon,name='modify_icon'),
]