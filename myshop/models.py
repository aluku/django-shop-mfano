from datetime import datetime
from shop.models import Product
from django.db import models

# Create your models here.
class Item(Product):
    category = models.ForeignKey('CatalogCategory', related_name='items')
    description = models.TextField()
    photo = models.ImageField(upload_to='item_photo', blank=True)
    manufacturer = models.CharField(max_length=300, blank=True)

    def __unicode__(self):
        return u'%s' % self.name

    @models.permalink
    def get_absolute_url(self):
        return ('shop:product_detail', (), {'slug': self.slug})

    class Meta:
        pass

class Catalog(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=150, unique=True)
    publisher = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    pub_date = models.DateTimeField(default=datetime.now)

    def __unicode__(self):
        return u'%s' % self.name

class CatalogCategory(models.Model):
    catalog = models.ForeignKey('Catalog', related_name='categories')
    parent = models.ForeignKey('self', blank=True, null=True,
                               related_name='children')
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=150)
    description = models.TextField(blank=True)

    def __unicode__(self):
        if self.parent:
            return u'%s: %s - %s' % (self.catalog.name,
                                     self.parent.name,
                                     self.name)
        return u'%s: %s' % (self.catalog.name, self.name)
		
    class Meta:
	    ordering = ["catalog"]

class ItemDetail(models.Model):
    item = models.ForeignKey('Item', related_name='details')
    attribute = models.ForeignKey('ItemAttribute')
    value = models.CharField(max_length=500)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return u'%s: %s' % (self.product, self.attribute)

class ItemAttribute(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return u'%s' % self.name