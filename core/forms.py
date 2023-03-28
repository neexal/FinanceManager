from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')
        widgets = {
            'password1': forms.PasswordInput(attrs={'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
        }



class LoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email', max_length=254, widget=forms.EmailInput(attrs={'autofocus': True}))
    password = forms.CharField(label='Password', strip=False, widget=forms.PasswordInput)

    error_messages = {
        'invalid_login': "Please enter a correct email and password. Note that both fields may be case-sensitive.",
        'inactive': "This account is inactive.",
    }
