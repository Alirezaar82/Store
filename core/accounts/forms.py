from django.contrib.auth import forms as form_auth ,get_user_model

from . import models

class CustomeAuthenticationForm(form_auth.AuthenticationForm):
    pass

class CustomeCreateFrom(form_auth.UserCreationForm):
    class Meta:
        model = models.CustomeUser
        fields = ('phone_number',)