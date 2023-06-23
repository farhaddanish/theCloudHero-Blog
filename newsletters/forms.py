from django import forms
from django.db import models
from django import forms
from .models import Subscribers


class SubscribersForm (forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = ['email']

        # def clean_email(self):
        #     email = self.cleaned_data.get('email')
        #     return email.lower()
