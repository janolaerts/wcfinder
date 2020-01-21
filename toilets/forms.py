from django import forms
from . import models

class AddToilet(forms.ModelForm):
  #remarks = forms.CharField(required = False, widget = forms.Textarea( attrs = { 'placeholder': 'I.e. clean, accessible for wheelchairs, etc.' } ))
  number = forms.IntegerField(required = False)

  class Meta:
    model = models.Toilet
    fields = ['city', 'street', 'number', 'price', 'cleaned', 'wheelchair_accessible' ]

class EditToilet(forms.ModelForm):
  class Meta:
    model = models.Toilet
    fields = ['city', 'street', 'number', 'price', 'cleaned', 'wheelchair_accessible' ]