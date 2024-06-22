from django import forms
from accounts.models import UserAddressModel

class UserAddressForm(forms.ModelForm):
    class Meta:
        model = UserAddressModel
        fields= [
            'name',
            "address",
            "state",
            "city",
            "zip_code",
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control '
        self.fields['state'].widget.attrs['class'] = 'form-control '
        self.fields['city'].widget.attrs['class'] = 'form-control '
        self.fields['zip_code'].widget.attrs['class'] = 'form-control '
        self.fields['address'].widget.attrs['class'] = 'form-control '

