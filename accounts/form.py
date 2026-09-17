from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.EmailInput(
            attrs={"class": "input-field pl-10", "required": True, "autocomplete": "on"}
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "input-field pl-10 pr-10", "required": True}
        )
    )
