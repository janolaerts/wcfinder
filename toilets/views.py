from django.shortcuts import render
from . models import Toilet
from . import forms

# Create your views here.
def filter_cities(toilet):
  return toilet.city

def wclist_view(request):
  city = request.GET.get('city')
  toilet_list = Toilet.objects.filter(city=city)
  return render(request, 'toilets/wc_list.html', { 'toilets': toilet_list})

def add_toilet_view(request):
  form = forms.AddToilet(request.POST)
  return render(request, 'toilets/add_toilet.html', { 'form': form })