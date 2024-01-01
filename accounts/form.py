from django import forms
from .models import users


class UserSignupForm(forms.ModelForm):
    password2 =  forms.CharField(max_length=255, min_length=8, widget=forms.PasswordInput())
    class Meta:
        model = users
        fields = ('mobile_phone', 'password', 'password2')


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