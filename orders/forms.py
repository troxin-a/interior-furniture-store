import re
from django import forms
from django.contrib import messages


class CreateOrderForm(forms.Form):

    first_name = forms.CharField()
    last_name = forms.CharField(required=False)
    phone_number = forms.CharField()
    delivery_address = forms.CharField(required=False)

    def clean_phone_number(self):
        """Валидация номера телефона"""
        data = self.cleaned_data['phone_number']

        pattern = re.compile(r'\+7\s?[\(]{0,1}9[0-9]{2}[\)]{0,1}\s?\d{3}[-]{0,1}\d{2}[-]{0,1}\d{2}')
        if not pattern.match(data):
            raise forms.ValidationError("Неверный формат номера")

        return data
