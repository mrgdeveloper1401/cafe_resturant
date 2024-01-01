from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import View
from .models import users
from .form import UserSignupForm, Loginform, AcceptUserForm



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
            form.save()
            messages.success(request, 'Account created successfully please enter code for active accounts','success')
            return redirect('accounts:accept_user')
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
                return redirect('all_products:home')
            messages.error(request, 'mobile phone or password is incorrect', 'error')
        return render(request, self.template_name, {'form': form})


class AcceptUserView(View):
    form_class = AcceptUserForm
    template_name = 'accounts/accept_user.html'
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    def post(self, request, *args, **kwargs):
        pass