from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.views import View


class HomeView(View):
    def get(self, request):
        return render(request ,'products/index.html')

class ProductListView(View):
    def get(self, request):
        product = Product.objects.all()
        return render(request, 'products/all_products.html', {'product': product})

class ProductDetailsView(View):
    def get(self, request, *args, **kwargs):
        details_product = get_object_or_404(Product, slug=kwargs['slug'])
        return render(request, 'products/product_details.html', {'details_product': details_product})

def category_partial(request, *args, **kwargs):
    category = Category.objects.filter(is_active=True)
    return render(request, 'products/category_partial.html', {'category': category})

def site_header(request, *args, **kwargs):
    return render(request, 'products/site_header.html')

def site_footer(request, *args, **kwargs):
    return render(request, 'products/site_footer.html')