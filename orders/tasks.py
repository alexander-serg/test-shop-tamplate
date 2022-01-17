from celery.app import shared_task
from django.core.mail import send_mail

from banny_shop.celery import app
from .models import Order


@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = 'Заказ № {}'.format(order_id)
    message = 'Dear {},\n\nYou have successfully placed an order.\
                Your order id is {}.'.format(order.first_name, order.id)
    mail_sent = send_mail(subject,
                          message,
                          'karandashsou@gmail.com',
                          [order.email])
    return mail_sent