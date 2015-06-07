from django.conf.urls import patterns, include, url
from shop import urls as shop_urls

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'example.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout',{'next_page': 'welcome'}),
    (r'^accounts/', include('allauth.urls')),
    url(r'^shop/', include('myshop.urls', namespace="shop")),
    url(r'^shop/', include(shop_urls)),
)
