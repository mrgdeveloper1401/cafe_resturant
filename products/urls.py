from django.urls import path, re_path
from .views import ProductListView, ProductDetailsView, HomeView, category_partial, site_header \
    ,ProductFuturedView

app_name = 'products'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('all_product/', ProductListView.as_view(), name='all_product'),
    re_path(r'^product/(?P<slug>[-\w]+)/$', ProductDetailsView.as_view(), name='product_detail'),
    # path('site_header/', site_header, name='site_header'),
    # path('futured_products/', ProductFuturedView.as_view(), name='futured_products'),
]
