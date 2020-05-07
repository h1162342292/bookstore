from django.core.cache import cache
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.decorators.cache import cache_page

from book.models import BookType, IndexBookImage, IndexSaleImage, Book, HistoryBook
from bookstore.settings import MEDIA_URL

@cache_page(60 * 5)
def index(request):
    type = BookType.objects.all()
    banners = IndexBookImage.objects.all().order_by('index')
    sales = IndexSaleImage.objects.all().order_by('index')
    books = Book.objects.filter(is_index=True).all().order_by('-sales')
    return render(request, 'book/index.html', locals())
def book_detail(request,gid):
    try:
        book = Book.objects.get(pk=gid)
    except:
            return redirect(reverse('book:index'))
    type = BookType.objects.all()
    new_books = Book.objects.all().order_by('-add_time')
    history = HistoryBook.objects.filter(user=request.user).all()
    for i in history:
        if i.book == book:
            i.number +=1
            i.save()
            break
    else:
        HistoryBook.objects.create(book=book,user=request.user)
    return render(request,'book/detail.html',locals())
def book_type(request,tid):
    books = Book.objects.filter(type_id=tid).all()
    type = BookType.objects.all()
    new_books = Book.objects.all().order_by('-add_time')
    return render(request,'book/type.html',locals())
def search(request):
    new_books = Book.objects.all().order_by('-add_time')
    search_text = request.GET.get('search',default=None)
    print(search_text)
    all_book = []
    books = Book.objects.all()
    print(type(books))
    if search_text:
        for book in books:
            if search_text in book.name:
                all_book.append(book)
                return JsonResponse({'status':200})
    print(all_book)
    return render(request,'book/search.html',locals())