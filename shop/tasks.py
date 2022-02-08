from __future__ import absolute_import, unicode_literals
# from celery import shared_task
from django.core.mail import send_mail

# from b_shop.celery import app
from .models import Messages, MessagesDetail, Item

# @shared_task
def call_request(form_id):
    form_message = Messages.objects.get(id=form_id)
  
    subject = 'Заказан звонок № {}'.format(form_id)
    message = 'Номер телефона: {}'.format(form_message.phone)
    mail_sent = send_mail(subject,
                          message,
                          'testlastnametestname59@gmail.com',
                          ['testlastnametestname59@gmail.com'])
    return mail_sent

def message_detail(itpm_id, form_id):
	product = Item.objects.get(id=itpm_id)
	form_detail = MessagesDetail.objects.get(id=form_id)
	subject = 'Заказан звонок по товару {}'.format(product.name)
	message = 'Имя: {}\
            	Номер телефона: {}\
        		Сообщение: {}'.format( form_detail.name, form_detail.phone, form_detail.message)
	mail_sent = send_mail(subject,
                          message,
                          'testlastnametestname59@gmail.com',
                          ['testlastnametestname59@gmail.com'])
	return mail_sent
