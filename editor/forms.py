from django import forms


class UserSearchForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=50)