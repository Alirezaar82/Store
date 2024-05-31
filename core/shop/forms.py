from django import forms
from .models import ReviewModel,ProductModel,ProductStatusType
from django.utils.translation import gettext as _

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewModel
        fields = ['product', 'description', 'rate']
        error_messages = {
            'description': {
                'required': _('The description field is required'),
            },
        }
    def clean(self):
        cleaned_data = super().clean()
        product = cleaned_data.get('product')

        # Check if the product exists and is published
        try:
            ProductModel.objects.get(id=product.id,status=ProductStatusType.publish.value)
        except ProductModel.DoesNotExist:
            raise forms.ValidationError(_('This product does not exist'))

        return cleaned_data