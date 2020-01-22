from django import forms
from . import models

class AddToilet(forms.ModelForm):
  number = forms.IntegerField(required = False)

  class Meta:
    model = models.Toilet
    fields = ['city', 'street', 'number', 'price_in_EUR', 'cleaned', 'wheelchair_accessible' ]

class EditToilet(forms.ModelForm):
  number = forms.IntegerField(required = False)

  class Meta:
    model = models.Toilet
    fields = ['city', 'street', 'number', 'price_in_EUR', 'cleaned', 'wheelchair_accessible' ]