from django.shortcuts import render
from django.http import HttpResponse
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         post=item['item'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            order_created(order.id, cart)
            return render(request, 'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'orders/order/create.html',
                      {'cart': cart, 'form': form})


