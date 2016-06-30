# coding with UTF-8

from django import forms
from django.contrib.auth.models import User
from bootstrap_toolkit.widgets import BootstrapDateInput, BootstrapTextInput, BootstrapUneditableInput


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label=u"username",
        error_messages = {'required': 'input username'},
        widget=forms.TextInput(
            attrs={
                'placeholder': u"username",
            }
        ),
    )
    password = forms.CharField(
        required=True,
        label=u"password",
        error_messages={'required': u'input password'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder': u"password",
            }
        ),
    )

    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u"password and username is required")
        else:
            cleaned_data = super(LoginForm, self).clean()
