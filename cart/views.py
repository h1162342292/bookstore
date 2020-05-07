from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from cart.models import Cart

import decimal
def add_cart(request):
    bid = request.GET.get('bookId')
    print(bid)
    number = request.GET.get('number')
    total = request.GET.get('total')
    flag = False
    if Cart.objects.filter(book_id=bid,user=request.user).count()>0:
        cart = Cart.objects.get(book_id=bid,user=request.user)
        cart.number += int(number)
        total1 = float(cart.total)
        total = float(total)+total1
        cart.total = total
        cart.save()
        flag = True
    else:
        cart = Cart.objects.create(book_id=bid,user=request.user,number=number,total=total)
        if cart:
            flag = True
    if flag:
        count = Cart.objects.filter(user=request.user).count()
        return JsonResponse({'status':'200','count':count})
    else:
        return JsonResponse({'status':'401'})
def show_cart(request):
    carts = Cart.objects.filter(user=request.user).all()
    count = carts.count()
    return render(request,'cart/cart.html',locals())
def delete_cart(request):
    bid = request.GET.get('bid')
    cart = Cart.objects.filter(book_id=bid,user=request.user).first()
    cart.delete()
    return redirect(reverse('cart:show'))
def add_num(request):
    number = request.GET.get('number')
    book_id = request.GET.get('book_id')
    cart = Cart.objects.filter(book_id=book_id, user=request.user).first()
    cart.number = number
    cart.total = decimal.Decimal(number)*cart.book.price
    cart.save()
    return JsonResponse({'status':200})