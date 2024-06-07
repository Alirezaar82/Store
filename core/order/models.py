from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from django.core.validators import MaxValueValidator, MinValueValidator

from decimal import Decimal

user = get_user_model()

class CouponModel(models.Model):
    code = models.CharField(max_length=255)
    discount_percent = models.IntegerField(default=0,validators = [MinValueValidator(0),MaxValueValidator(100)])
    max_limit_usage = models.PositiveIntegerField(default=10)
    used_by = models.ForeignKey(user,on_delete=models.PROTECT)
    expiration_date = models.DateTimeField(null=True,blank=True)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-datetime_created"]

    def __str__(self):
        return f'{self.code} {self.discount_percent}' 

    def get_usage_all(self):
        return self.used_by.all().count()

class OrderStatusType(models.IntegerChoices):
    pending = 1,_('pending')
    success = 2,_('success')
    faild = 3,_('faild')

class OrderModel(models.Model):
    user = models.ForeignKey(user,on_delete=models.PROTECT)
    status = models.IntegerField(choices=OrderStatusType.choices,default=OrderStatusType.pending.value,)
    
    address = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip_code = models.CharField(default='0')

    # payment = models.ForeignKey()

    total_price = models.DecimalField(default=0,max_digits=10,decimal_places=0)

    coupon = models.ForeignKey(CouponModel,on_delete=models.PROTECT,null=True,related_name='orders')


    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-datetime_created"]
    
    def __str__(self):
        return f'{self.user},{self.id}'

    def get_status(self):
        return {
            "id":self.status,
            "title":OrderStatusType(self.status).name,
            "label":OrderStatusType(self.status).label,
        }
    def get_full_address(self):
        return f'state={self.state},city={self.city},address={self.address},zip_code={self.zip_code}'
    
    def get_price(self):
        
        if self.coupon:            
            return round(self.total_price - (self.total_price * Decimal( self.coupon.discount_percent /100)))
        else:
            return self.total_price
        
    def calculate_total_price(self):
        return sum(item.price * item.quantity for item in self.order_items.all())
    
    @property
    def is_successful(self):
        return self.status == OrderStatusType.success.value
    

class OrderItem(models.Model):
    order = models.ForeignKey(OrderModel,on_delete=models.CASCADE)
    product = models.ForeignKey('shop.ProductModel',on_delete=models.CASCADE)
    
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(default=0,max_digits=10,decimal_places=0)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-datetime_created"]

    def __str__(self):
        return f'{self.order},{self.product}'
  
