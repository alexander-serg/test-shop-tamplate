from django.db import models
from shop.models import Item
from django.db.models.signals import post_save

class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Статус {}'.format(self.name)

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

class Order(models.Model):
    first_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=48, blank=True, null=True,default=None)
    email = models.EmailField()
    city = models.CharField(max_length=100)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING, related_name='статус',)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return  'Заказ {0} статус {1}'.format(self.id, self.status.name)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    def save(self, *args, **kwargs):

        super(Order, self).save(*args, **kwargs)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.DO_NOTHING)
    post = models.ForeignKey(Item, blank=True, null=True, default=None, on_delete=models.DO_NOTHING, related_name='order_items')
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    # def get_cost(self):
    #     return self.price_per_item * self.quantity

    def save(self, *args, **kwargs):
        price_per_item = self.post.price
        self.price_per_item = price_per_item
        self.total_price = self.quantity * price_per_item

        super(OrderItem, self).save(*args, **kwargs)

def orderItem_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_items_in_order = OrderItem.objects.filter(order=order)

    order_total_price = 0
    for i in all_items_in_order:
        order_total_price += i.total_price

    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)

post_save.connect(orderItem_post_save, sender=OrderItem)