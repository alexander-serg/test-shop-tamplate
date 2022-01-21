from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddItemForm
from .models import *

menu = [
    {'title': "Условия проката", 'url_name': 'service'},
    {'title': "Каталог", 'url_name': 'inst'},
    {'title': "Контакты", 'url_name': 'contact'}
    #     {'title': "Войти", 'url_name': 'login'}
]


def item_list(request):
    posts = Item.objects.filter(is_published=True)
    image_dress = ItemImage.objects.filter(is_published=True, is_main=True)

    context = {
        'posts': posts,
        'image_dress': image_dress,
        'menu': menu,
        'title': 'Каталог товаров',
    }

    return render(request, 'shop/item_list.html', context=context)

def item_detail(request, post_slug):
    itpm = get_object_or_404(Item, slug=post_slug)
    photos = ItemImage.objects.filter(itpm=itpm, is_main=False)
    mainphoto = ItemImage.objects.filter(itpm=itpm, is_main=True)
    cart_product_form = CartAddItemForm()
    context = {
        'itpm': itpm,
        'photos': photos,
        'mainphoto': mainphoto,
        'menu': menu,
        'cart_product_form': cart_product_form,
        'title': itpm.name,
    }

    return render(request, 'shop/detail.html', context=context)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def about(request):
    return render(request, 'shop/about.html', {'menu': menu, 'title': 'О сайте'})


def service(request):
    return HttpResponse("Условия проката")

def contact(request):
    return HttpResponse("Обратная связь")

def inst(request):
    return HttpResponse("inst.com")




