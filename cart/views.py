from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Item
from .cart import Cart
from .forms import CartAddItemForm

@require_POST
def cart_add(request, post_id):
    cart = Cart(request)
    post = get_object_or_404(Item, id=post_id)
    form = CartAddItemForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(post=post,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')

def cart_remove(request, post_id):
    cart = Cart(request)
    post = get_object_or_404(Item, id=post_id)
    cart.remove(post)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})
