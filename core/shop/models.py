from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from django.core.validators import MaxValueValidator, MinValueValidator


from decimal import Decimal

user = get_user_model()

class ProductCategoryModel(models.Model):
    name = models.CharField(verbose_name=_('name'),max_length=255)
    slug = models.SlugField(verbose_name=_('slug'),unique=True,allow_unicode=True)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-datetime_created"]

    def __str__(self):
        return self.name
    
class ProductStatusType(models.IntegerChoices):
    publish = 1,_('publish')
    draft = 2,_('draft')
    
class ProductModel(models.Model):
    user = models.ForeignKey(user,on_delete=models.CASCADE,related_name=_('user'))
    category = models.ManyToManyField(ProductCategoryModel,verbose_name=_('product category'))

    title = models.CharField(verbose_name=_('title'),max_length=255)
    slug = models.SlugField(verbose_name=_('slug'),unique=True,allow_unicode=True)
    image = models.ImageField(upload_to='shop/img',default='shop/img/default.png')
    description = models.TextField()
    brief_description = models.TextField(null=True,blank=True)
    price = models.DecimalField(default=0,max_digits=10,decimal_places=0)
    
    stock = models.PositiveIntegerField(default=0)
    status = models.IntegerField(choices=ProductStatusType.choices,default=ProductStatusType.draft.value)
    discount_percent = models.IntegerField(default=0,validators = [MinValueValidator(0),MaxValueValidator(100)])
    
    # avg_rate = models.FloatField(default=0.0)
    
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_update = models.DateTimeField(auto_now=True)

    
    class Meta:
        ordering = ["-datetime_created"]

    def is_published(self):
        if self.status == ProductStatusType.publish.value:
            return True
        else:
            return False
        
    def get_price_discounted(self):        
        discount_amount = self.price * Decimal(self.discount_percent / 100)
        discounted_amount = self.price - discount_amount
        return round(discounted_amount)
    
    def is_discounted(self):
        return self.discount_percent != 0
    
    def get_price(self):
        if self.is_discounted():
            return self.get_price_discounted()
        else:
            return self.price
        
class ProductImages(models.Model):
    product = models.ForeignKey(ProductModel,on_delete=models.CASCADE,verbose_name=_('product'),related_name='images')
    file = models.ImageField(upload_to='shop/extra/',verbose_name=_('file'))

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_update = models.DateTimeField(auto_now=True)

class WishlistProductModel(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.PROTECT)
    product = models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.product.title