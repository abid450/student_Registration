from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django.core import validators

class register_y(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your name'}))
    email = forms.EmailField(label='Email Address',widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter your Email'}),validators=[validators.MinLengthValidator(24)])
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your Password'}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Confirm your Password'}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class change_U(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter your Email'}))
    date_joined = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'placeholder':'Date Joined'}))
    last_login = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'placeholder':'Last Login'}))
    is_active = forms.CheckboxInput()
    password = None
    class Meta:
        model = User
        fields = ['username','email','date_joined','last_login','is_active']
