from django import forms
from .models import Messages, MessagesDetail
from django.utils.translation import gettext_lazy as _

class MessagesForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['phone']
        labels = {
            'phone': _(''),
        }
        help_texts = {
            'phone': _(''),
        }

        widgets = {
            'phone': forms.TextInput
                           (attrs={'placeholder':'Номер телефона'}),
        }

class MessagesDetailForm(forms.ModelForm):
    class Meta:
        model = MessagesDetail
        fields = ['name', 'phone', 'message']
        lables = {
            'name': _(''),
            'phone': _(''),
            'message': _('')
        }
        help_texts = {
            'name': _(''),
            'phone': _(''),
            'message': _('')
        }
        widgets = {
            'name': forms.TextInput
                    (attrs={'placeholder': 'Имя'}),
            'phone': forms.TextInput
                           (attrs={'placeholder':'Номер телефона'}),
            'message': forms.Textarea(attrs={'rows':4, 'cols':15, 'placeholder':'Сообщение'}),
                 
        }