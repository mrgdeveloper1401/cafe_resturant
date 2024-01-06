from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib import messages
from .forms import ContactUsForm
from .models import ContactUs, WaysofCommunication


class ContactUsView(View):
    form_class = ContactUsForm
    templated_name = 'contact/contact_us.html'
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.templated_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            ContactUs.objects.create(**form.cleaned_data)
            messages.success(request, 'پیام شما با موفقیت برای ما ارسال شد به زودی با شما تماس خواهیم گرفت')
            return redirect('contacts:contact_us')
        else:
            messages.error(request, 'خطا در ارسال فورم ها')
            return render(request, self.templated_name, {'form': form})
        
class WaysOfCommunication(View):
    def get(self, request, *args, **kwargs):
        woc = WaysofCommunication.objects.all()
        return render(request, 'contact/ways_of_communication.html', {'woc': woc})
    