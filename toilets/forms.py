from django import forms
from . import models

class AddToilet(forms.ModelForm):
  #clean = forms.BooleanField(required = False, label = "Clean") 
  #accessible = forms.BooleanField(required = False, label = "Wheelchair")

  class Meta:
    model = models.Toilet
    fields = ['city', 'street', 'number', 'reference', 'price']