from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import View
from .models import users
from .form import UserSignupForm, Loginform, AcceptUserForm
from random import randint
from caffe.utils import send_otp_code
from .models import OtpCode
from datetime import timedelta



class UserSignupView(View):
    form_class = UserSignupForm
    template_name = 'accounts/signup.html'
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('all_products:home')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            random_code = randint(0, 99999)
            send_otp_code(cd['mobile_phone'], random_code)
            OtpCode.objects.create(mobile_phone=cd['mobile_phone'], code=random_code)
            request.session['user_signup_info'] ={
                'mobile_phone': cd['mobile_phone'],
                'password': cd['password'],
            }
            messages.success(request, 'ما کدی به شماره موبایل شما وارد کردیم لطفا برای وارد شدن و فعال سازی حساب خود ان را تایید نمایید', 'sucess')
            return redirect('accounts:accept_user')
        return render(request, self.template_name, {'form': form})


class AcceptUserView(View):
    form_class = AcceptUserForm
    template_name = 'accounts/accept_user.html'
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    def post(self, request, *args, **kwargs):
        user_session = request.session['user_signup_info']
        otp_code = OtpCode.objects.get(mobile_phone=user_session['mobile_phone'])
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(int(cd['code']) == otp_code.code)
            if int(cd['code']) == otp_code.code:
                users.objects.create_user(
                    mobile_phone=user_session['mobile_phone'],
                    password=user_session['password']
                )
                messages.success(request, 'حساب شما با موفقیت ساخته شد لطفا برای  ادامه پروفایل خود رو تکمیل نمایید', 'success')
                otp_code.delete()
                del user_session
                return redirect('accounts:login')
            else:
                messages.error(request, 'کد تایید شما اشتباه است', 'danger')
                return render(request, self.template_name, {'form': form})
        return render(request, self.template_name, {'form': form})
        


class UserLoginView(View):
    form_class = Loginform
    template_name = 'accounts/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('all_products:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                mobile_phone=cd['mobile_phone'],
                password=cd['password'],
            )
            if user is not None:
                login(request, user)
                messages.success(request, 'successfully logged in', 'success')
                return redirect('accounts:profile', request.user.id)
            messages.error(request, 'mobile phone or password is incorrect', 'error')
        return render(request, self.template_name, {'form': form})
