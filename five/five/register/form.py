from django import forms

from django.contrib.auth.models import User
from register.models import UserModels

class userform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())


    class Meta():
        model=User
        fields=('username','email','password')


class userformsinfo(forms.ModelForm):
    class Meta():
        model=UserModels
        fields=('site','pics')