from django import forms
from . import models

class AddToilet(forms.ModelForm):
  remarks = forms.CharField(required = False, widget = forms.Textarea( attrs = { 'placeholder': 'I.e. clean, accessible for wheelchairs, etc.' } ))

  class Meta:
    model = models.Toilet
    fields = ['city', 'street', 'number', 'reference', 'price', 'remarks' ]

#class UpdateToilet(forms.ModelForm):
  #class Meta:
    #model = models.Toilet
    #fields = ['city', 'street', 'number', 'reference', 'price', 'remarks' ]