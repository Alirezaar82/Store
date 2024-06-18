from django import forms


from .models import ContactUsModel

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUsModel
        fields = ["subject","first_name","last_name","email","phone_number","description"]
        
        error_messages = {
            'email': {
                'required': "فیلد ایمیل نمی تواند خالی باشد"
            },
            'description': {
                'required': "فیلد محتوا نمی تواند خالی باشد",
                'min_length': "طول محتوای وارد شده غیر مجاز است"
            },
            'subject': {
                'required': "فیلد  عنوان نمی تواند خالی باشد"
            },
            'first_name': {
                'required': "فیلد نام نمی تواند خالی باشد"
            },
            'last_name': {
                'required': "فیلد نام خانوادگی نمی تواند خالی باشد"
            }
        }