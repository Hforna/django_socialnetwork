from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class FormUser(forms.ModelForm):
    password2 = forms.CharField(max_length=256, required=False)

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


    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password')
        password2 = cleaned_data.get("password2")
        if password1 != password2:
            raise ValidationError({
                'password2': 'Passwords must be equals'
            })
