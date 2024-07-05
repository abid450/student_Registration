from django import forms
from django.core import validators

class yellow_form(forms.Form):


    Name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Name'}))
    Email = forms.EmailField(label='Email Address',widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter your Email'}),validators=[validators.MinLengthValidator(24)])
    Course = [
        ("Office Management", "Office Management"),
        ("Grapics Design", "Grapics Design"),
        ("Web Development", "Web Development"),
        ("Python Programming", "Python Programming"),
        ("Digital Marketing", "Digital Marketing")
    ]
    Course = forms.ChoiceField(label='Course Name', choices=Course, widget=forms.Select(attrs={'class':'form-control','placeholder':'Select your Coure'}))
    Phone = forms.CharField(label='Phone Number',widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'+880'}),validators=[validators.MaxLengthValidator(11),validators.MinLengthValidator(11)])
    College = forms.CharField(label='School/College Name',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter School/College','rows':4,'cols':32}))

    def clean_Name(self):
        name = self.cleaned_data['Name']
        if len(name)<5:
            raise forms.ValidationError('Incorrect Name, Please Enter your Correct Name')
        return name

    