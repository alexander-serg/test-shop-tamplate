from __future__ import absolute_import, unicode_literals
# from celery import shared_task
from django.core.mail import send_mail

# from b_shop.celery import app
from .models import Order

# @shared_task
def order_created(order_id, cart):
    order = Order.objects.get(id=order_id)
    product_names = ''
    for items in cart:
        product_names += items['item'].name

    subject = 'Заказ № {}'.format(order_id)
    message = 'Получен заказ на {},\n\nИмя: {}\
                Номер телефона: {}\
                Сообщение: {}'.format(product_names, order.first_name, order.phone, order.message)
    mail_sent = send_mail(subject,
                          message,
                          'testlastnametestname59@gmail.com',
                          ['testlastnametestname59@gmail.com'])
    return mail_sent