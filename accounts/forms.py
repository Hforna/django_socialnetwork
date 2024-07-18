from typing import Any, Mapping
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList


def add_attr(field_name, widget_attr, text_in_widget):
    existing = field_name.widget.attrs.get(widget_attr, "")
    field_name.widget.attrs[widget_attr] = f'{existing} {text_in_widget}'.strip()

class FormUser(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_attr(self.fields["username"], "placeholder", "Username")

    password = forms.CharField(widget=forms.PasswordInput, max_length=256, required=False)
    password2 = forms.CharField(widget=forms.PasswordInput, max_length=256, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

    labels = {
        'username': 'Username',
        'email': 'Digit your best e-mail',
        'password': 'Password',
        'password2': 'Repeat your password'
    }

    error_messages = {
        'username': {'required': 'Username is required', 'max_length': 'The username is very long'}
    }

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        exists = User.objects.filter(email=email).exists()

        if exists:
            raise ValidationError(
                'User e-mail is already in use', code='invalid',
            )

        return email
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password')
        password2 = cleaned_data.get("password2")
        if password1 != password2:
            raise ValidationError({
                'password2': 'Passwords must be equals'
            })
