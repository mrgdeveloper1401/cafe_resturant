from django.urls import path
from .views import ContactView, ContactToUs


app_name = 'contacts'
urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path('contact_to_us/', ContactToUs.as_view(), name='contact_to_us'),
]
