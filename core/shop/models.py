from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.db.models import Avg
from jalali_date import jdatetime



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
    category = models.ManyToManyField(ProductCategoryModel,verbose_name=_('product_category'))

    title = models.CharField(verbose_name=_('title'),max_length=255)
    slug = models.SlugField(verbose_name=_('slug'),unique=True,allow_unicode=True)
    image = models.ImageField(upload_to='shop/img',default='shop/img/default.png')
    description = models.TextField()
    brief_description = models.TextField(null=True,blank=True)
    price = models.DecimalField(default=0,max_digits=10,decimal_places=0)

    sold = models.PositiveIntegerField(null=True,blank=True)
    stock = models.PositiveIntegerField(default=0)
    status = models.IntegerField(choices=ProductStatusType.choices,default=ProductStatusType.draft.value)
    discount_percent = models.IntegerField(default=0,validators = [MinValueValidator(0),MaxValueValidator(100)])
    
    avg_rate = models.FloatField(default=0.0)
    
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_update = models.DateTimeField(auto_now=True)

    
    class Meta:
        ordering = ["-datetime_created"]

    def __str__(self):
        return self.title

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
    def get_categories(self):
        return ", ".join([category.name for category in self.category.all()])
    
    def get_status(self):
        return {
            "id":self.status,
            "title":ProductStatusType(self.status).name,
            "label":ProductStatusType(self.status).label,
        }
        
        
class ProductImages(models.Model):
    product = models.ForeignKey(ProductModel,on_delete=models.CASCADE,verbose_name=_('product'),related_name='product_images')
    file = models.ImageField(upload_to='shop/extra/',verbose_name=_('file'))

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_update = models.DateTimeField(auto_now=True)

class WishlistProductModel(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.PROTECT)
    product = models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.product.title
    
class ReviewStatusType(models.IntegerChoices):
    pending = 1,_('pending')
    accepted = 2,_('accepted')
    rejected = 3,_('rejected')

class ReviewModel(models.Model):
    user = models.ForeignKey(user,on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel,on_delete=models.CASCADE)
        
    description = models.TextField()
    rate = models.PositiveIntegerField()
    status = models.IntegerField(choices=ReviewStatusType.choices,default=ReviewStatusType.pending.value)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-datetime_created"]

    def __str__(self):
        return f'{self.user},{self.product}'

    def is_accepted(self):
        if self.status == ReviewStatusType.accepted.value:
            return True
        else:
            return False

    def get_status(self):
        return {
            "id":self.status,
            "title":ReviewStatusType(self.status).name,
            "label":ReviewStatusType(self.status).label,
        }
         

@receiver(post_save,sender=ReviewModel)
def calculate_avg_review(sender,instance,created,**kwargs):
    if instance.status == ReviewStatusType.accepted.value:
        product = instance.product
        average_rating = ReviewModel.objects.filter(product=product, status=ReviewStatusType.accepted).aggregate(Avg('rate'))['rate__avg']
        product.avg_rate = round(average_rating,1)
        product.save()


