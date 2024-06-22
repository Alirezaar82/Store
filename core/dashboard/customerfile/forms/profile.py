from django import forms

from accounts.models import Profile

class CustomerProfileEditForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields =[
            "first_name",
            "last_name",
            "email"
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'نام خود را وارد نمایید'
        self.fields['last_name'].widget.attrs['class'] = 'form-control '
        self.fields['last_name'].widget.attrs['placeholder'] = 'نام خانوادگی را وارد نمایید'
        self.fields['email'].widget.attrs['class'] = 'form-control text-center'
        self.fields['email'].widget.attrs['placeholder'] = 'ایمیل را وارد نمایید'
        
        
class CustomerProfileImageEditForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields =[
            'image',
        ]
        
        