from django.shortcuts import render, get_object_or_404
from .models import Food, Category
from django.views import View


class HomeView(View):
    def get(self, request):
        return render(request ,'food/index.html')

class FoodListView(View):
    def get(self, request):
        foods = Food.objects.all()
        return render(request, 'food/all_products.html', {'foods': foods})

class ProductDetailsView(View):
    def get(self, request, *args, **kwargs):
        details_food = get_object_or_404(Food, slug=kwargs['slug'])
        return render(request, 'food/product_details.html', {'details_food': details_food})

def category_partial(request, *args, **kwargs):
    category = Category.objects.filter(is_active=True)
    return render(request, 'food/category_partial.html', {'category': category})

def site_header(request, *args, **kwargs):
    return render(request, 'food/site_header.html')

def site_footer(request, *args, **kwargs):
    return render(request, 'food/site_footer.html')