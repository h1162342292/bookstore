from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
loginRequired_list = ['/user/center','/user/order','/user/address','/cart/add', '/cart/show', '/order/generate',
                      '/order/commit','/order/comment']

class LoginMiddleware(MiddlewareMixin):
    def process_request(self,request): #process_request 进入视图函数之前调用动作 | process_response 视图函数执行完毕之后调用方法
        if request.path in loginRequired_list:
            if not request.user.is_authenticated:#判断用户是否登录
                return redirect(reverse('user:login'))
