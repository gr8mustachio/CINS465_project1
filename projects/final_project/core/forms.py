from django import forms
from django.core import validators
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class JoinForm(forms.ModelForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'size' : '30'}))
    password = forms.CharField(widget= forms.TextInput(attrs={'autocomplete' : 'new-password'}))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
        help_texts = {
            'username' : None
        }