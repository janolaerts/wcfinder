from django import forms
from . import models

class AddToilet(forms.ModelForm):
  clean = forms.BooleanField(required = False, label = "Is the toilet clean?")
  accessible = forms.BooleanField(required = False, label = "Is the toilet accessible for wheelchairs?")

  class Meta:
    model = models.Toilet
    fields = ['city', 'street', 'number', 'reference', 'price']