#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from bootstrap_toolkit.widgets import BootstrapDateInput, BootstrapTextInput, BootstrapUneditableInput


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label=u"用户名：",
        error_messages={'required': u'请输入用户名'},
        widget=forms.TextInput(
            attrs={
                'placeholder': u"username",
            }
        ),
    )
    password = forms.CharField(
        required=True,
        label=u"密码：",
        error_messages={'required': u'请输入密码'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder': u"password",
            }
        ),
    )

    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u"请检查输入")
        else:
            cleaned_data = super(LoginForm, self).clean()


class FindpaswdForm(forms.Form):
    username = forms.CharField(
        required=True,
        label=u"用户名：",
        error_messages={'required': u'请输入用户名'},
        widget=forms.TextInput(
            attrs={
                'placeholder': u"username",
            }
        ),
    )
    mailaddress = forms.CharField(
        required=True,
        label=u"邮箱：",
        error_messages={'required': u'请输入邮箱'},
        widget=forms.TextInput(
            attrs={
                'placeholder': u"e-mail",
            }
        ),
    )
    newpassword = forms.CharField(
        required=True,
        label=u"新密码：",
        error_messages={'required': u'请输入新密码'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder': u"password",
            }
        ),
    )


    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u"请检查输入")
        else:
            cleaned_data = super(FindpaswdForm, self).clean()


class  NewaccountForm(forms.Form):
    username = forms.CharField(
        required=True,
        label=u"用户名：",
        error_messages={'required': u'请输入用户名'},
        widget=forms.TextInput(
            attrs={
                'placeholder': u"username",
            }
        ),
    )
    mailaddress = forms.CharField(
        required=True,
        label=u"邮箱：",
        error_messages={'required': u'请输入邮箱'},
        widget=forms.TextInput(
            attrs={
                'placeholder': u"e-mail",
            }
        ),
    )
    setpassword = forms.CharField(
        required=True,
        label=u"密码：",
        error_messages={'required': u'请输入密码'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder': u"password",
            }
        ),
    )


    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u"请检查输入")
        else:
            cleaned_data = super(NewaccountForm, self).clean()