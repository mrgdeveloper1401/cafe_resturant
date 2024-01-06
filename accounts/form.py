from django import forms
from .models import User
from django.utils.translation import gettext_lazy as _


class UserSignupForm(forms.ModelForm):
    password2 = forms.CharField(max_length=255, min_length=8, widget=forms.PasswordInput(attrs={'class':'input_second input_all', 'placeholder':'تکرار رمز عبور'}), label='تکرار رمز عبور')
    class Meta:
        model = User
        fields = ('mobile_phone', 'password')
        
        widgets = {
            'mobile_phone': forms.TextInput(attrs={'class':'input_second input_all', 'placeholder':'شماره همراه: 09171234567'}),
            'password': forms.PasswordInput(attrs={'class':'input_second input_all', 'placeholder': 'رمز عبور: 12345678'}),
        }
        
        labels = {
            'password': _('رمز عبور'),
        }
        
        error_messages = {
            'mobile_phone': {
                'unique': 'شماره موبایل قبلا وجود دارد'
            }
        }
        
    def clean_password2(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('رمز عبور با تکرار آن مطابقت ندارد')
        return password2
        

class Loginform(forms.Form):
    mobile_phone = forms.CharField(max_length=11,label='شمار موبایل',
                                   widget=forms.TextInput(attrs={'class': 'input_second input_all', 'placeholder': 'لطفا شماره موبایل خود را وارد کنید'}),
                                   error_messages={
                                       'required':'لطفا شماره همراه خود را وارد کنید'
                                   })
    password = forms.CharField(max_length=255,
                               min_length=8,
                               label='رمز عبور',
                               widget=forms.PasswordInput(attrs={'class': 'input_second input_all', 'placeholder': 'رمز عبور خود را وارد کنید'}),
                               error_messages={
                                   'required':'لطفا پسورد خود را وارد کنید'
                               })


class AcceptUserForm(forms.Form):
    code = forms.CharField(max_length=5, widget=forms.TextInput(attrs={'class': 'input_second input_all', 'placeholder': 'کد تایید'}))


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