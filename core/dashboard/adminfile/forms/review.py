from django import forms
from django.core.exceptions import ValidationError

from shop.models import ReviewModel

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewModel
        fields=[            
            'status',
        ]
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['status'].widget.attrs['class'] = 'form-select'
