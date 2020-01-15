from django.shortcuts import render
from toilets.models import Toilet

def filter_cities(toilet):
  return toilet.city

def citylist_view(request):
  toilet_list = Toilet.objects.all()
  cities = list(map(filter_cities, toilet_list))
  filtered_cities = list(set(cities))
  return render(request, 'city_list.html', { 'cities': sorted(filtered_cities) })