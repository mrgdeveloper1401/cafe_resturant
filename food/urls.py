from django.urls import path, re_path
from .views import FoodListView, ProductDetailsView, HomeView, CategoryView

app_name = 'food'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('all_product/', FoodListView.as_view(), name='all_product'),
    re_path(r'^product/(?P<slug>[-\w]+)/$', ProductDetailsView.as_view(), name='product_details'),
    path('category/', CategoryView.as_view(), name='category'),
]
