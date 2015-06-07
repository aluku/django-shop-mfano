from django.shortcuts     import render, get_object_or_404
from django.http          import HttpResponse, Http404
from django.views.generic import ListView, DetailView, View
from myshop.models        import *

# Create your views here.

class ProductList(ListView):
	model = Product
	paginate_by = 12
	
class ProductDetail(DetailView):
	template_name = "shop/product_detail.html"
	model = Product
	slug = 'slug'

class CatalogProducts(ListView):
    template_name = "shop/catalog_products.html"
    model = Product
    paginate_by = 12
	
    def get_queryset(self):
        self.catalog_id = self.kwargs.get('catalog_id', None)
        queryset = Product.objects.filter(category = CatalogCategory.objects.filter(catalog_id=self.catalog_id))
        return queryset

class NewProducts(ListView):
    template_name = "shop/welcome.html"
    model = Product
    paginate_by = 4

    def get_queryset(self):
        queryset = Product.objects.order_by('-date_added')[:8]
        return queryset