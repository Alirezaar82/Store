from django import forms
from shop.models import ReviewModel

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewModel
        fields = [
            "description",
            "rate",
            "status",
        ] 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['description'].disabled = True
        self.fields['description'].required = False
        self.fields['rate'].widget.attrs['class'] = 'form-control '
        self.fields['rate'].required = False
        self.fields['rate'].disabled = True
        self.fields['status'].widget.attrs['class'] = 'form-select'