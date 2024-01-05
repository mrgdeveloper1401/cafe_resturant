from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib import messages
from .forms import ContactForm
from .models import Contact


class ContactView(View):
    form_class = ContactForm
    template_name = 'contact/contact_us.html'
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent', 'success')
            return redirect('contacts:contact')
        return render(request, self.template_name, {'form': form})


class ContactToUs(View):
    def get(self, request):
        contact_to_us = Contact.objects.filter(is_active=True)
        return render(request, 'contact/contact_to_us.html', {'contact_to_us': contact_to_us})