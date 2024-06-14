from django import forms
from django.core.exceptions import ValidationError

from shop.models import ProductCategoryModel

class CategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategoryModel
        fields=[            
            'name',
            'slug',
        ]
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['name'].widget.attrs['class'] = 'form-control'
            self.fields['slug'].widget.attrs['class'] = 'form-control'

