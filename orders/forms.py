from django import forms
from .models import Order
from django.utils.translation import gettext_lazy as _



class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        
        fields = ['first_name', 'phone', 'message']
        labels = {
            'first_name': _(''),
            'phone': _(''),
            'message': _(''),
        }
        help_texts = {
            'first_name': _(''),
            'phone': _(''),
            'message': _(''),
        }

        widgets = {
            'first_name': forms.TextInput
                           (attrs={'placeholder':'Ваше имя'}),
            'phone': forms.TextInput
                           (attrs={'placeholder':'Номер телефона'}),
            'message': forms.Textarea(attrs={'rows':4, 'cols':15, 'placeholder':'Сообщение'}), 
        }