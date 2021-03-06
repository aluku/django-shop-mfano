from django.conf.urls import patterns, url, include
from django.contrib import admin
from myshop.models import *
from django.views.generic import TemplateView
from myshop.views import ProductList, ProductDetail, NewProducts #, CatalogProducts

admin.autodiscover()

urlpatterns = patterns('myshop',
    #url(r'^products/$', 'object_list', {'queryset': Product.objects.all()}, name='product_list'),
    #url(r'^product/(?P<slug>[-\w]+)/$', 'object_detail',{'queryset': Product.objects.all()},name='product_detail'),
    url(r'^products/$', ProductList.as_view(), name="product-list"),
    url(r'^welcome/$', NewProducts.as_view(), name="welcome"),
    # url(r'^products/$', ProductList.as_view(), name="product_list"),
    url(r'^products/(?P<slug>[-\w]+)/$', ProductDetail.as_view(), name="product-detail"),
	#url(r'^catalog/(?P<catalog_id>[-\d]+)/$', CatalogProducts.as_view(), name="catalog_products"),
    url(r'^accounts/', include('allauth.urls')),
    #url(r'^search/$', Search.as_view(), name="Search"),
    url(r'^search/', include('haystack.urls')),
)
