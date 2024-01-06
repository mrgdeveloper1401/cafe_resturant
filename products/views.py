from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView

class HomeView(TemplateView):
    template_name = 'products/index.html'


class ProductListView(View):
    def get(self, request):
        product = Product.objects.filter(is_active=True)
        return render(request, 'products/all_products.html', {'product': product})


class ProductFuturedView(ListView):
    model = Product
    queryset = Product.objects.filter(is_active=True).order_by('-sell_price')[:10]
    template_name = 'products/futured_products.html'
    context_object_name = 'product_futured'


class ProductDetailsView(View):
    def get(self, request, *args, **kwargs):
        details_product = get_object_or_404(Product, slug=kwargs['slug'])
        return render(request, 'products/product_details.html', {'details_product': details_product})

class ProductDetailsView(DetailView):
    template_name = 'products/product_details.html'
    context_object_name = 'details_product'
    model = Product


def category_partial(request, *args, **kwargs):
    category = Category.objects.filter(is_active=True)
    return render(request, 'products/category_partial.html', {'category': category})


def site_header(request, *args, **kwargs):
    return render(request, 'products/site_header.html')


def site_footer(request, *args, **kwargs):
    return render(request, 'products/site_footer.html')
