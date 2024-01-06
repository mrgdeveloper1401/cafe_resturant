from django import forms
from .models import User
from django.utils.translation import gettext_lazy as _


class UserSignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('mobile_phone', 'password')
        
        widgets = {
            'mobile_phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'شماره همراه: 09171234567'}),
            'password': forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'رمز عبور: 12345678'}),
        }
        
        lable = {
            'passwprd': _('رمز عبور'),
        }
        
        error_messages = {
            'mobile_phone': {
                'unique': 'شماره موبایل قبلا وجود دارد'
            }
        }
        

class Loginform(forms.Form):
    mobile_phone = forms.CharField(max_length=11,
                                   widget=forms.TextInput(),
                                   error_messages={
                                       'required':'لطفا شماره همراه خود را وارد کنید'
                                   })
    password = forms.CharField(max_length=255,
                               min_length=8,
                               widget=forms.PasswordInput(),
                               error_messages={
                                   'required':'لطفا پسورد خود را وارد کنید'
                               })


class AcceptUserForm(forms.Form):
    code = forms.CharField(max_length=5, widget=forms.TextInput())


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'mobile_phone',
            'bio',
            'address',
        )
        
        widgets = {
           'mobile_phone': forms.TextInput(attrs={'class':'form-control col-md-6', 'placeholder':'شماره همراه: 09171234567'}),
            'bio': forms.Textarea(attrs={'class':'form-control col-md-6', 'placeholder':'توضیحات شما'}),
            'address': forms.Textarea(attrs={'class':'form-control col-md-6', 'placeholder':'آدرس'}),
            'first_name': forms.TextInput(attrs={'class':'form-control col-md-6', 'placeholder':'نام'}),
            'last_name': forms.TextInput(attrs={'class':'form-control col-md-6', 'placeholder':'نام خانوادگی'}),
            'email': forms.EmailInput(attrs={'class':'form-control col-md-6', 'placeholder':'ایمیل'}),
            }

class PasswordResetForm(forms.Form):
    mobile_phone = forms.CharField(max_length=11, widget=forms.TextInput())