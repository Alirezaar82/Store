from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

class UserForm(forms.ModelForm):
    # phone_number = forms.CharField(
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control mx-3 Disabled text-center mb-3',
    #         'disabled': 'disabled',
            

    #     })
    # )
    class Meta:
        model = User
    
        fields = [
            "phone_number",
            "is_active",
            "is_verified",
            "type",
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone_number'].widget.attrs['class'] = 'form-control mx-3 Disabled text-center mb-3'
        self.fields['phone_number'].disabled = True
        self.fields['phone_number'].required = False
        self.fields['is_active'].required = False
        self.fields['is_active'].widget.attrs['class'] = 'form-check-input mb-3'
        self.fields['is_verified'].required = False
        self.fields['is_verified'].widget.attrs['class'] = 'form-check-input mb-3'
        self.fields['type'].required = False
        self.fields['type'].widget.attrs['class'] = 'form-select'
        