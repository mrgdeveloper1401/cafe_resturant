from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import View
from .models import users
from .form import UserSignupForm, Loginform, AcceptUserForm, ProfileForm, PasswordResetForm
from random import randint
from caffe.utils import send_otp_code
from .models import OtpCode
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetCompleteView, PasswordResetConfirmView


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
            after_time = timezone.now() + timedelta(seconds=120)
            if int(cd['code']) == otp_code.code:
                if timezone.now() < after_time:
                    users.objects.create_user(
                        mobile_phone=user_session['mobile_phone'],
                        password=user_session['password']
                    )
                    messages.success(request, 'حساب شما با موفقیت ساخته شد لطفا برای  ادامه پروفایل خود رو تکمیل نمایید', 'success')
                    otp_code.delete()
                    del user_session
                    return redirect('accounts:login')
                else:
                    messages.error(request, 'مدت زمان برای تایید کد شما گذشته هست لطفا دوباره درخواست بدهید')
                    return redirect('accounts:signup')
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
                return redirect('food:home')
            messages.error(request, 'mobile phone or password is incorrect', 'error')
        return render(request, self.template_name, {'form': form})

class Logout(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, 'successfully logged out','success')
        return redirect('accounts:login')


class PasswordResetV(PasswordResetView):
    template_name = 'accounts/password_reset_view.html'
    success_url = reverse_lazy('accounts:password_reset_done')
    email_template_name = 'password_reset_email.html'


class PasswordResetDoneView(PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'


class PasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')


class PasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'


class ProfileView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        profile = get_object_or_404(users, pk=kwargs['pk'])
        return render(request, 'accounts/profile.html', {'profile': profile})


class ProfileEditView(LoginRequiredMixin, View):
    form_class = ProfileForm
    def get(self, request, *args, **kwargs):
        form = self.form_class(instance=request.user)
        return render(request, 'accounts/profile_edit.html', {'profile': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'successfully updated','success')
            return redirect('accounts:profile', pk=request.user.id)
        return render(request, 'accounts/profile_edit.html', {'profile': form})