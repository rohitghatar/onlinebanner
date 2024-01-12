from django import forms
from .models import *


class client_Signup_form(forms.ModelForm):
    class Meta:
        model=client_signup
        fields='__all__'


class publisher_Signup_form(forms.ModelForm):
    class Meta:
        model=publisher_signup
        fields='__all__'


class banners_upload_form(forms.ModelForm):
    class Meta:
        model=banners_upload
        fields='__all__'


class client_Update_form(forms.ModelForm):
    class Meta:
        model=client_signup
        fields=['firstname','lastname','email','mobile','city']


class publisher_Update_form(forms.ModelForm):
    class Meta:
        model=publisher_signup
        fields=['firstname','lastname','email','mobile','city']

    
class feedbackForm(forms.ModelForm):
    class Meta:
        model=feedback
        fields='__all__'