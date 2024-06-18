from django import forms
from django.core.exceptions import ValidationError

from order.models import CouponModel

class CouponForm(forms.ModelForm):
    expiration_date = forms.DateTimeField(required=False,widget=forms.DateTimeInput(attrs={'class': 'form-control','type':'datetime-local'}))

    class Meta:
        model = CouponModel
        fields=[            
            'code',
            'discount_percent',
            'max_limit_usage',
            'used_by',
            'expiration_date',
        ]
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['code'].widget.attrs['class'] = 'form-control'
            self.fields['used_by'].widget.attrs['class'] = 'form-control'
            self.fields['max_limit_usage'].widget.attrs['class'] = 'form-control'
            self.fields['discount_percent'].widget.attrs['class'] = 'form-control'
