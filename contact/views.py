from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib import messages
from .forms import ContactUsForm
from .models import WaysofCommunication
from django.views.generic import FormView


class ContactUsView(FormView):
    form_class = ContactUsForm
    template_name = 'contact/contact_us.html'
    success_url = '/contact_us/'
    
    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'درخواست شما با موفقیت برای ما ارسال شد بزودی با شما تماس خواهیم گرفت', 'success')
        return super().form_valid(form)


class WaysOfCommunication(View):
    def get(self, request, *args, **kwargs):
        woc = WaysofCommunication.objects.all()
        return render(request, 'contact/ways_of_communication.html', {'woc': woc})