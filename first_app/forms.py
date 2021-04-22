from django import forms


class UserForm(forms.Form):
    login = forms.CharField()
    password = forms.IntegerField(widget=forms.PasswordInput)