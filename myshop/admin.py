from django.contrib import admin
from myshop.models import *


class CatalogAdmin(admin.ModelAdmin):
    list_display = ('name', 'publisher', 'description', 'pub_date')
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Catalog, CatalogAdmin)

class CatalogCategoryAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'description', 'parent')
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(CatalogCategory, CatalogCategoryAdmin)
    
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category')
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Item, ItemAdmin)

class ItemDetailAdmin(admin.ModelAdmin):
    list_display = ('item', 'attribute', 'value')
admin.site.register(ItemDetail, ItemDetailAdmin)

class ItemAttributeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
admin.site.register(ItemAttribute, ItemAttributeAdmin)

