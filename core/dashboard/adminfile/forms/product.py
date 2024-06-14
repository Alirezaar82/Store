from django import forms
from django.core.exceptions import ValidationError

from shop.models import ProductModel

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields=[            
            'category', 
            'title',
            'slug',
            'image',
            'description',
            'brief_description',
            'price',
            'stock',
            'status',
            'discount_percent',
        ]
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['title'].widget.attrs['class'] = 'form-control'
            self.fields['slug'].widget.attrs['class'] = 'form-control'
            self.fields['category'].widget.attrs['class'] = 'form-control'
            self.fields['image'].widget.attrs['class'] = 'form-control'
            self.fields['brief_description'].widget.attrs['class'] = 'form-control'
            self.fields['description'].widget.attrs['class'] = 'form-control'
            self.fields['description'].widget.attrs['id'] = 'ckeditor'
            self.fields['stock'].widget.attrs['class'] = 'form-control'
            self.fields['stock'].widget.attrs['type'] = 'number'
            self.fields['status'].widget.attrs['class'] = 'form-select'
            self.fields['price'].widget.attrs['class'] = 'form-control'
            self.fields['discount_percent'].widget.attrs['class'] = 'form-control'


    def clean_brief_description(self):
        brief_description = self.cleaned_data.get('brief_description')
        if len(brief_description) > 255:
            raise ValidationError(".توضیحات کوتاه نمی‌تواند بیش از ۲۵۵ کاراکتر باشد")
        return brief_description

