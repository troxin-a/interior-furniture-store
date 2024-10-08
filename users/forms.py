from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UserChangeForm,
)
from users.models import User


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User

    username = forms.CharField()
    password = forms.CharField()


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )

    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()


class UserEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "image",
            "first_name",
            "last_name",
            "phone_number",
            "delivery_address",
            "email",
        )

        image = forms.ImageField(required=False)
        first_name = forms.CharField()
        last_name = forms.CharField()
        phone_number = forms.CharField()
        delivery_address = forms.CharField()
        email = forms.CharField()
