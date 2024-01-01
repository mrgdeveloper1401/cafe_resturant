from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from .forms import ContactForm


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
