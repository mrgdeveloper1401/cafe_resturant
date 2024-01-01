from django import forms
from .models import Contact
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ('create_at', 'update_at')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control',}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, }),
            'mobile_phone': forms.TextInput(attrs={'class': 'form-control'}),
        }
        # lable = {
        #     'first_name': _('نام'),
        #     'last_name': _('نام خانوادگی'),
        #     'email': _('ایمیل'),
        #     'body': _('متن'),
        # }
        error_messages = {
            'first_name': {
              'required': 'نام را وارد کنید',
            },
            'last_name': {
              'required': 'نام خانوادگی را وارد کنید',
            },
            'email': {
              'required': 'ایمیل را وارد کنید',
            },
            'body': {
              'required': 'متن را وارد کنید',
            },
            'mobile_phone': {
                'required': 'شماره همراه خود را وارد کنید'
            }
        }