from django.urls import path, re_path
from .views import FoodListView, ProductDetailsView

app_name = 'food'
urlpatterns = [
    path('', FoodListView.as_view(), name='home'),
    re_path(r'^product/(?P<slug>[-\w]+)/$', ProductDetailsView.as_view(), name='product_details'),
]
