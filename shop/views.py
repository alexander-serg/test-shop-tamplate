from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from cart.forms import CartAddItemForm
from .models import *
from .forms import MessagesForm, MessagesDetailForm
from .tasks import call_request, message_detail

menu = [
    {'title': "Акции", 'url_name': 'action'},
    {'title': "Распродажа", 'url_name': 'sale'}, 
    {'title': "Условия проката", 'url_name': 'rental'},
    {'title': "Контакты", 'url_name': 'contact'},
]


def item_list(request):
    posts = Item.objects.filter(is_published=True)
    image_dress = ItemImage.objects.filter(is_published=True, is_main=True)
    item_wedd = image_dress.filter(itpm__category__id=1)
    item_evn = image_dress.filter(itpm__category__id=2)
    item_child = image_dress.filter(itpm__category__id=3)
    reviews = Reviews.objects.filter(is_published=True)
    form = MessagesForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form = form.save()
            call_request(form.id)
            return render(request, 'shop/item_list_message.html',)        
    
    context = {
        'posts': posts,
        'image_dress': image_dress,
        'item_child': item_child,
        'item_wedd': item_wedd,
        'item_evn': item_evn,
        'reviews': reviews,
        'menu': menu,
        'title': 'Каталог товаров',
        'form': form,
    }

    return render(request, 'shop/item_list.html', context=context)

def item_detail(request, post_slug):
    itpm = get_object_or_404(Item, slug=post_slug)
    photos = ItemImage.objects.filter(itpm=itpm, is_main=False)
    mainphoto = ItemImage.objects.filter(itpm=itpm, is_main=True)
    cart_product_form = CartAddItemForm()
    form_detail = MessagesDetailForm(request.POST or None)
    if request.method == 'POST':
        if form_detail.is_valid():
            form_detail = form_detail.save()
            message_detail(itpm.id, form_detail.id)
            return render(request, 'shop/detail_message.html',) 
    context = {
        'itpm': itpm,
        'photos': photos,
        'mainphoto': mainphoto,
        'menu': menu,
        'cart_product_form': cart_product_form,
        'title': itpm.name,
        'form_detail': form_detail,
    }

    return render(request, 'shop/detail.html', context=context)

def pageNotFound(request, exception):
    context = {
    'menu': menu,
    'title': 'Страница не найдена',
    }
    return render(request, 'shop/pagenotfound.html', context=context)

def sale(request):
    context = {
    'menu': menu,
    'title': 'Распродажа',
    }
    return render(request, 'shop/sale.html', context=context)


def action(request):
    posts = Item.objects.filter(is_published=True)
    image_dress = ItemImage.objects.filter(is_published=True, is_main=True)
    paginator = Paginator(image_dress, 8)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'posts': posts,
        'image_dress': image_dress,
        'menu': menu,
        'title': 'Товары по акции',
    }

    return render(request, 'shop/action.html', context=context)

def contact(request):
    context = {
    'menu': menu,
    'title': 'Контакты',
    }
    return render(request, 'shop/contact.html', context=context)

def rental(request):
    context = {
    'menu': menu,
    'title': 'Условия проката',
    }
    return render(request, 'shop/rental.html', context=context)

def wedding_dress(request):
    
    posts = Item.objects.filter(is_published=True)
    image_dress = ItemImage.objects.filter(is_published=True, is_main=True)
    item_wedd = image_dress.filter(itpm__category__id=1)
    paginator = Paginator(item_wedd, 8)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'posts': posts,
        'image_dress': image_dress,
        'item_wedd': item_wedd,
        'menu': menu,
        'title': 'Свадебные платья',
    }

    return render(request, 'shop/catalog/catalog1.html', context=context)

def evening_dress(request):
   
    posts = Item.objects.filter(is_published=True)
    image_dress = ItemImage.objects.filter(is_published=True, is_main=True)
    item_evn = image_dress.filter(itpm__category__id=2)
    paginator = Paginator(item_evn, 8)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'posts': posts,
        'image_dress': image_dress,
        'item_evn': item_evn,
        'menu': menu,
        'title': 'Вечерние платья',
    }

    return render(request, 'shop/catalog/catalog2.html', context=context)

def child_dress(request):
    
    posts = Item.objects.filter(is_published=True)
    image_dress = ItemImage.objects.filter(is_published=True, is_main=True)
    item_child = image_dress.filter(itpm__category__id=3)
    paginator = Paginator(item_child, 8)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'posts': posts,
        'image_dress': image_dress,
        'item_child': item_child,
        'menu': menu,
        'title': 'Детские платья',
    }

    return render(request, 'shop/catalog/catalog3.html', context=context)








