from django import forms
from django.core import validators
from django.contrib.auth.models import User

valid_cols = ["a", "b","c", "d", "e", "f", "g", "h"]
valid_rows = ["1", "2", "3", "4", "5", "6", "7", "8"]

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())

class JoinForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}))
    email = forms.CharField(widget = forms.TextInput(attrs={'size': '30'}))
    class Meta:
        model=User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
        help_texts = {
            'username': None
        }

def validate_location(loc):
    if(len(loc) > 2) or (loc[0] not in valid_cols) or (loc[1] not in valid_rows):
        raise forms.ValidationError("Use row and column format for the piece to be moved i.e: 'a2' or 'f7'.")

def validate_new_loc(new_loc):
    if(len(new_loc) > 2) or (new_loc[0] not in valid_cols) or (new_loc[1] not in valid_rows):
        raise forms.ValidationError("Use row and column format for the piece's new position i.e: 'a2' or 'f7'.")

class ChessForm(forms.Form):
    location=forms.CharField(min_length=2, max_length=2, strip=True,
    widget=forms.TextInput(attrs={'placeholder': 'a2','style':'font-size:small', 'style':'text-transform:lowercase;'}),
    validators=[validators.MinLengthValidator(2),
    validators.MaxLengthValidator(2),
    validate_location])
    new_location = forms.CharField(min_length=2, max_length=2, strip=True,
    widget=forms.TextInput(attrs={'placeholder': 'c4', 'style':'font-size:small',  'style':'text-transform:lowercase;'}),
    validators=[validators.MinLengthValidator(2),
    validators.MaxLengthValidator(2),
    validate_new_loc])
