from django import forms
from django.utils import timezone
from django.utils.translation import gettext as _

from accounts.models import UserAddressModel
from .models import CouponModel


class OrderCheckOutForm(forms.Form):
    address_id = forms.CharField(max_length=255)
    coupon = forms.CharField(max_length=255,required=False)
    

    error_messages = {
            'address_id': {
                'required': _('The address_id field is required'),
            },
            'coupon': {
                'required': _('The coupon field is required'),
            },
        }
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(OrderCheckOutForm, self).__init__(*args, **kwargs)
        
    def clean_address_id(self):
        address_id = self.cleaned_data.get('address_id')

        # Check if the address_id belongs to the requested user
        user = self.request.user  # Assuming the user is available in the request object
        try:
            address = UserAddressModel.objects.get(id=address_id, user=user)
        except UserAddressModel.DoesNotExist:
            raise forms.ValidationError("ادرس انتخاب شده درست نیست!!")

        return address
    
    def clean_coupon(self):
        code = self.cleaned_data.get('coupon')
        if code == "":
            return None
        
        user = self.request.user 
        coupon = None
        try:
            coupon = CouponModel.objects.get(code=code)
        except CouponModel.DoesNotExist:
            raise forms.ValidationError("کد تخفیف اشتباه است")
        if coupon:

            if coupon.used_by.count() >= coupon.max_limit_usage:
                raise forms.ValidationError("محدودیت در تعداد استفاده")


            if coupon.expiration_date and coupon.expiration_date < timezone.now():
                raise forms.ValidationError("کد تخفیف منقضی شده است")


            if user in coupon.used_by.all():
                raise forms.ValidationError("این کد تخفیف قبلا توسط شما استفاده شده است")

        return coupon
