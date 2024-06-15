from django import forms

from website.models import LogoModel

class LogoForm(forms.ModelForm):
    class Meta:
        model = LogoModel
        fields=[            
           'logo'
        ]
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['logo'].widget.attrs['class'] = 'form-control'

