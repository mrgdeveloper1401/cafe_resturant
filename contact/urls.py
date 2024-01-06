from django.urls import path
from .views import ContactUsView


app_name = 'contacts'
urlpatterns = [
    path('contact_us/', ContactUsView.as_view(), name='contact_us'),
]
