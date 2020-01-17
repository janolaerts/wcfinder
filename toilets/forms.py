from django import forms
from . import models

class AddToilet(forms.ModelForm):

  class Meta:
    model = models.Toilet
    fields = ['city', 'street', 'number', 'reference', 'price', 'clean' ]