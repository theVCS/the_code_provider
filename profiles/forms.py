from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class ProfileForm(forms.ModelForm):

    name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email_id = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email Id'}))

    class Meta:
        model = Profile
        fields = ('name', 'email_id')