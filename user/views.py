import uuid

import time

import hashlib
import requests
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from book.models import HistoryBook
from bookstore import settings
from order.models import Order
from user.models import UserProfile, UserAddress


def index(request):
    return render(request,'base.html')
def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('user_name')
        pwd = request.POST.get('pwd')
        phone = request.POST.get('phone')
        check = request.POST.get('allow')
        if check != 'on':
            render(request,'user/register.html',{'msg':'请同意用户协议'})
        pwd = make_password(password=pwd)
        user = UserProfile.objects.create(username=username,password=pwd,phone=phone,email=email)
        user.is_active = 0
        user.save()
        token = str(uuid.uuid4()).replace('-','')
        request.session[token] = user.id
        path = 'http://127.0.0.1:8000/user/active?token={}'.format(token)
        subject = '三岁书屋激活邮件'
        message = '''
        欢迎注册三岁书屋会员！亲爱的用户请赶快激活使用吧！
        <br>  <a href='{}'>点击激活</a>
        <br>
        如果链接不可用可以复制以下内容到浏览器激活：
        {}
        <br>
        <br>
                                    三岁书屋开发团队
        '''.format(path, path)
        send_mail(subject=subject,message='',from_email=settings.EMAIL_HOST_USER,recipient_list=[email,],html_message=message)
        return redirect(reverse('user:login'))
    return render(request,'user/register.html')
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('user_name')
        password = request.POST.get('pwd')
        rem_name = request.POST.get('rem_name')
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            response = redirect(reverse('book:index'))
            if rem_name == 'on':
                response.set_cookie('uname',username)
            return response
        else:
            return render(request,'user/login.html',{'errmsg':'用户名或密码错误或邮箱未激活'})
    else:
        username = request.COOKIES.get('uname')
        return render(request,'user/login.html',{'username':username})
def user_logout(request):
    logout(request)
    return redirect(reverse('book:index'))
def check_user(request):
    username = request.GET.get('username')
    user = UserProfile.objects.filter(username=username).first()
    if user:
        return JsonResponse({'status':'fail','msg':'用户名已存在'})
    else:
        return JsonResponse({'status':'success','msg':'用户名可用'})
def user_active(request):
    token = request.GET.get('token')
    print(token)
    uid = request.session.get(token)
    print(uid)
    user = UserProfile.objects.get(pk=uid)
    user.is_active = 1
    user.save()
    return redirect(reverse('user:login'))
def forget_password(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        code = request.POST.get('code')
        if request.session.get(phone) == code:
            return render(request,'user/modify_pwd.html',{'phone':phone})
    return render(request,'user/forget_password.html')
def send_check(request):
    phone = request.GET.get('phone')
    url = 'https://api.netease.im/sms/sendcode.action'
    headers = {}
    headers['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8'
    headers['AppKey'] = 'acf6ac8afe2e4137295a54368dc6a266'
    Nonce = str(uuid.uuid4()).replace('-', '')
    headers['Nonce'] = Nonce
    CurTime = str(int(time.time()))
    headers['CurTime'] = CurTime
    AppSecret = '462b302cc8fa'
    CheckSum = hashlib.sha1((AppSecret + Nonce + CurTime).encode('utf-8')).hexdigest()
    headers['CheckSum'] = CheckSum
    response = requests.post(url=url, data={'mobile': phone}, headers=headers)

    json_result = response.json()
    if json_result.get('code') == 200:
        request.session[phone] = json_result.get('obj')
        return JsonResponse({'msg': '短信发送成功！'})
    else:
        return JsonResponse({'msg': '短信发送失败!'})
def modify_pwd(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        pwd = request.POST.get('pwd')
        password = make_password(password=pwd)
        user = UserProfile.objects.filter(phone=phone).first()
        user.password = password
        user.save()
        return redirect(reverse('user:login'))
    return render(request,'user/modify_pwd.html')
def modify_icon(request):
    uid = request.POST.get('uid')
    icon = request.FILES.get('icon')
    user = UserProfile.objects.get(pk=uid)
    user.icon = icon
    user.save()
    return JsonResponse({'msg':'ok','image':str(user.icon)})
def user_center(request):
    histories = HistoryBook.objects.filter(user=request.user).order_by("-number")
    address = UserAddress.objects.filter(is_default=True, user=request.user).first()
    if address:
        return render(request, 'user/user_center.html', locals())
    else:
        address = UserAddress.objects.filter(user=request.user).first()
        return render(request, 'user/user_center.html', locals())


def user_order(request):
    orders = Order.objects.filter(user=request.user).order_by('-add_time')
    for order in orders:
        for status in Order.ORDER_STATUS:
            if order.order_status in status:
                order.status = status[1]
                break
    paginator = Paginator(orders,2)
    page = request.GET.get('page','1')
    try:
        page = int(page)
    except Exception as err:
        page = 1

    page_obj = paginator.page(page)
    return render(request, 'user/user_order.html',{'page_obj':page_obj})
def user_address(request):
    if request.method == 'POST':
        receiver = request.POST.get('receiver')
        addr = request.POST.get('addr')
        zipcode = request.POST.get('zipcode')
        phone = request.POST.get('phone')
        user_address = UserAddress.objects.create(receiver=receiver,address=addr,code=zipcode,phone=phone,user=request.user)
        if user_address:
            return redirect(reverse('user:address'))
        else:
            return render(request,'user/user_address.html',{'errmsg':'地址添加失败'})
    else:
        address = UserAddress.objects.filter(is_default=True,user=request.user).first()
        return render(request,'user/user_address.html',{'address':address})