from decimal import Decimal
from django.conf import settings
from shop.models import Item

class Cart(object):

    def __init__(self, request):
       self.session = request.session
       cart = self.session.get(settings.CART_SESSION_ID)
       if not cart:
           cart = self.session[settings.CART_SESSION_ID] = {}
       self.cart = cart

    def add(self, post, quantity=1, update_quantity=False):
        post_id = str(post.id)
        if post_id not in self.cart:
            self.cart[post_id] = {'quantity': 0,
                                  'price': str(post.price)}
        if update_quantity:
            self.cart[post_id]['quantity'] = quantity
        else:
            self.cart[post_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, post):
        post_id = str(post.id)
        if post_id in self.cart:
            del self.cart[post_id]
            self.save()

    def __iter__(self):
        post_ids = self.cart.keys()
        posts = Item.objects.filter(id__in=post_ids)
        for post in posts:
            self.cart[str(post.id)]['item'] = post

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in
                   self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True