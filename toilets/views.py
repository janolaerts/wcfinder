from django.shortcuts import render, redirect
from . models import Toilet
from . import forms
from django.http import HttpResponse

# Create your views here.
def filter_cities(toilet):
  return toilet.city

def wclist_view(request):
  city = request.GET.get('city')
  toilet_list = Toilet.objects.filter(city=city)
  return render(request, 'toilets/wc_list.html', { 'toilets': toilet_list })

def add_toilet_view(request):
  form = forms.AddToilet(request.POST)

  if request.method == 'POST':
    if form.is_valid():
      toilet = form.save()
      return render(request, 'toilets/toilet_added.html', { 'toilet': toilet })
      
  return render(request, 'toilets/add_toilet.html', { 'form': form })

def delete_toilet_view(request):
  id = request.GET.get('id')
  Toilet.objects.filter(id=id).delete()

  city = request.GET.get('city')
  toilet_list = Toilet.objects.filter(city=city)
  return render(request, 'toilets/wc_list.html', { 'toilets': toilet_list })