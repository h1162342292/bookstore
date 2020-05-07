from datetime import datetime

from alipay import AliPay
from django.db import transaction
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from bookstore import settings
from cart.models import Cart
from book.models import Book, BookType
from order.models import Order, OrderBooks
from user.models import UserAddress


def generate_order(request):
    gid_list = request.POST.getlist('goods_1')
    if not gid_list:
        return redirect(reverse('cart:show'))
    order_books_list = []
    books_order_number = 0
    books_order_total = 0
    # 遍历 商品id列表
    for gid in gid_list:
        # 商品对象
        book = Book.objects.get(pk=gid)
        # 去购物车获取该商品的信息
        cart_books = Cart.objects.get(book=book, user=request.user)
        # 动态设置商品的属性   获取购物车信息并将信息设置给商品对象
        book.number = cart_books.number
        book.total = cart_books.total
        # 添加到商品列表中
        order_books_list.append(book)

        # 该订单的所有商品的总数量和总价格
        books_order_number += cart_books.number
        books_order_total += cart_books.total

    # 写死运费
    carriage_price = 10
    # 真实付款价格
    real_pay_total = books_order_total + carriage_price

    # 收货地址
    addrs = UserAddress.objects.filter(user=request.user)
    # 辅助作用
    gid_list_str = ','.join(gid_list)

    return render(request, 'order/place_order.html', locals())


def order_commit(request):
    if request.method == 'POST':
        addrId = request.POST.get('addrId')
        pay_method = request.POST.get('pay_method')
        gid_list_str = request.POST.get('gid_list')
        books_order_total = request.POST.get('books_order_total')
        carriage_price = request.POST.get('carriage_price')
        books_order_number = request.POST.get('books_order_number')
        total = str(float(books_order_total)+float(carriage_price))
        print(total)
        if not all([addrId, pay_method, gid_list_str]):
            return JsonResponse({'status': '401', 'msg': '参数不完整'})
        # 构建订单id
        order_id = datetime.now().strftime('%Y%m%d%H%M%S') + str(request.user.id)

        # 设置事务保存点
        save_id = transaction.savepoint()  # a1

        try:
            order = Order.objects.create(order_id=order_id, user=request.user, address_id=addrId,
                                         pay_method=pay_method, books_number=books_order_number,
                                         books_total=books_order_total, carriage_price=carriage_price,total=total)

            gid_list = gid_list_str.split(',')

            for gid in gid_list:
                try:
                    # 获取购物车商品
                    cart = Cart.objects.get(book_id=gid, user=request.user)

                    # 获取商品对象
                    books = Book.objects.get(pk=gid)

                except:
                    # 商品不存在
                    transaction.savepoint_rollback(save_id)
                    return JsonResponse({'status': '401', 'errmsg': '商品不存在'})

                # 判断商品数量是否大于库存量
                if cart.number > books.inventory:
                    transaction.savepoint_rollback(save_id)
                    return JsonResponse({'status': '401', 'msg': '库存不足'})

                # 添加订单商品
                OrderBooks.objects.create(order=order, books_id=gid, number=cart.number, price=books.price)

                # 修改商品库存
                books.inventory -= cart.number
                # 修改商品销量
                books.sales += cart.number
                # 保存修改
                books.save()

                # 删除购物车商品
                cart.delete()
        except Exception as err:
            transaction.savepoint_rollback(save_id)
            return JsonResponse({'status': '401', 'msg': '下单失败'})

        # 提交事务
        transaction.savepoint_commit(save_id)

        return JsonResponse({'status': '200', 'msg': '下单成功'})


def order_pay(request):
    order_id = request.POST.get('orderId')
    if not order_id:
        return JsonResponse({'status': '401', 'errmsg': '无效的订单编号'})
    try:
        order = Order.objects.get(user=request.user, order_id=order_id, pay_method=2, order_status=1)
    except:
        return JsonResponse({'status': '401', 'errmsg': '订单错误'})

    app_private_key_string = open(settings.PRIVATE_KEY).read()
    alipay_public_key_string = open(settings.PUBLIC_KEY).read()

    alipay = AliPay(
        appid="2016092300575166",
        app_notify_url=None,  # 默认回调url
        app_private_key_string=app_private_key_string,
        # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
        alipay_public_key_string=alipay_public_key_string,
        sign_type="RSA2",  # RSA 或者 RSA2
        debug=True  # 默认False
    )

    # 如果你是 Python 3的用户，使用默认的字符串即可
    subject = "三岁书屋" + str(order_id)

    # 电脑网站支付，需要跳转到https://openapi.alipay.com/gateway.do? + order_string
    order_string = alipay.api_alipay_trade_page_pay(
        out_trade_no=order_id,
        total_amount=str(order.total),
        subject=subject,
        return_url=None,
        notify_url=None  # 可选, 不填则使用默认notify url
    )

    url = 'https://openapi.alipaydev.com/gateway.do?'

    path = url + order_string

    return JsonResponse({'status': '200', 'pay_path': path})


def check_order(request):
    order_id = request.POST.get('orderId')
    if not order_id:
        return JsonResponse({'status': '401', 'errmsg': '无效的订单编号'})

    try:
        order = Order.objects.get(user=request.user, order_id=order_id, pay_method=2, order_status=1)
    except:
        return JsonResponse({'status': '401', 'errmsg': '订单错误'})

    app_private_key_string = open(settings.PRIVATE_KEY).read()
    alipay_public_key_string = open(settings.PUBLIC_KEY).read()

    alipay = AliPay(
        appid="2016092300575166",#    2016101500691009
        app_notify_url=None,  # 默认回调url
        app_private_key_string=app_private_key_string,
        # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
        alipay_public_key_string=alipay_public_key_string,
        sign_type="RSA2",  # RSA 或者 RSA2
        debug=True  # 默认False
    )

    while True:
        # 查询订单的支付状态
        response = alipay.api_alipay_trade_query(order_id)
        """
                response = {
                  "alipay_trade_query_response": {
                    "trade_no": "2017032121001004070200176844",
                    "code": "10000",  # 接口调用是否成功
                    "invoice_amount": "20.00",
                    "open_id": "20880072506750308812798160715407",
                    "fund_bill_list": [
                      {
                        "amount": "20.00",
                        "fund_channel": "ALIPAYACCOUNT"
                      }
                    ],
                    "buyer_logon_id": "csq***@sandbox.com",
                    "send_pay_date": "2017-03-21 13:29:17",
                    "receipt_amount": "20.00",
                    "out_trade_no": "out_trade_no15",
                    "buyer_pay_amount": "20.00",
                    "buyer_user_id": "2088102169481075",
                    "msg": "Success",
                    "point_amount": "0.00",
                    "trade_status": "TRADE_SUCCESS",   # 'WAIT_BUYER_PAY'
                    "total_amount": "20.00"
                  },
                  "sign": ""
                }
        """
        code = response.get('code')
        trade_status = response.get('trade_status')
        # 支付成功
        if code == '10000' and trade_status == 'TRADE_SUCCESS':
            trade_no = response.get('trade_no')
            order.trade_on = trade_no
            order.order_status = 2
            order.save()
            return JsonResponse({'status': '200', 'msg': '支付成功！'})
        # 支付接口有问题  或者 接口没有问题但是用户还没有支付成功
        elif code == '40004' or (code == '10000' and trade_status == 'WAIT_BUYER_PAY'):
            import time
            time.sleep(5)
            continue
        else:
            # print(code)
            # print(trade_status)
            return JsonResponse({'status': '401', 'errmsg': '付款失败'})


def order_comment(request):
    if request.method == 'POST':
        orderid = request.POST.get('order_id')
        if not orderid:
            return redirect(reverse('user:order'))
        try:
            order = Order.objects.get(user=request.user, order_id=orderid)
        except:
            return redirect(reverse('user:order'))

        count = int(request.POST.get('total_count'))
        for i in range(1, count + 1):
            orderbooks_id = request.POST.get('goods_' + str(i))
            comment = request.POST.get('content_' + str(i))

            orderbooks = OrderBooks.objects.get(pk=orderbooks_id)
            orderbooks.comment = comment
            orderbooks.save()

        order.order_status = 5
        order.save()
        return redirect(reverse('user:order'))
    else:
        orderid = request.GET.get('orderid')
        if not orderid:
            return redirect(reverse('user:order'))
        try:
            order = Order.objects.get(user=request.user, order_id=orderid)
        except:
            return redirect(reverse('user:order'))

        for status in Order.ORDER_STATUS:  # status = (1, '待付款')
            if order.order_status in status:
                order.status_name = status[1]
                break
        orderbooks_list = []
        for orderbooks in order.orderbooks_set.all():
            orderbooks.total = orderbooks.price * orderbooks.number
            orderbooks_list.append(orderbooks)
        print()
        return render(request, 'order/order_commemt.html', {'order': order, 'orderbooks_list': orderbooks_list})
