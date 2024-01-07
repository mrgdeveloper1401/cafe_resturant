from django import forms
from .models import ContactUs
from django.utils.translation import gettext_lazy as _

class ContactUsForm(forms.ModelForm):
  class Meta:
    model = ContactUs
    exclude = ('create_at', 'update_at')
    
    widgets = {
      'first_name': forms.TextInput(attrs={'class': 'input_second input_all'}),
      'last_name': forms.TextInput(attrs={'class': 'input_second input_all'}),
      'email': forms.EmailInput(attrs={'class': 'input_second input_all'}),
      'body': forms.Textarea(attrs={'class': 'input_second input_all input_textarea text-right'}),
      'be_answered': forms.CheckboxInput(attrs={'class': 'm-3'}),
      'image': forms.FileInput(),
      'mobile_phone': forms.TextInput(attrs={'class': 'input_second input_all'}),
    }
    
    error_message = {
      'first_name': {
        'required': 'نام اجباری میباشد'
      },
      'last_name': {
        'required': 'نام خانوادگی اجباری میباشد'
      },
      'email': {
        
       'required': 'ایمیل اجباری میباشد'
      },
      'body': {
      'required': 'متن اجباری میباشد'
      },
      'mobile_phone': {
        'required': 'ایمیل اجباری میباشد'
      }
      }

    enctype = 'multipart/form-data'