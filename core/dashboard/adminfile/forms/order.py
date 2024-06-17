from django import forms
from django.core.exceptions import ValidationError

from order.models import OrderModel

class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderModel
        fields=[            
            'shippinStatus',
        ]
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['shippinStatus'].widget.attrs['class'] = 'form-select'
