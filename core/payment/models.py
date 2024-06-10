from django.db import models
from django.utils.translation import gettext as _


class PaymentStatusType(models.IntegerChoices):
    pending = 1,_('pending')
    success = 2,_('success')
    failed = 3,_('failed')

class Paymentmodel(models.Model):
    authority_id = models.CharField(max_length=255)
    ref_id = models.BigIntegerField(blank=True,null=True)
    
    response_json = models.JSONField(default=dict)
    response_code = models.IntegerField(null=True,blank=True)

    status = models.IntegerField(choices=PaymentStatusType.choices,default=PaymentStatusType.pending.value)
    
    amount = models.DecimalField(default=0,max_digits=10,decimal_places=0)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_update = models.DateTimeField(auto_now=True)

    
    class Meta:
        ordering = ["-datetime_created"]

    def __str__(self):
        return f'{self.authority_id},{self.status}'
    
    