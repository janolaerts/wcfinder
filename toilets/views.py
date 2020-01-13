from django.shortcuts import render
from . models import Toilet

# Create your views here.
def filter_cities(toilet):
  return toilet.city

def wclist_view(request):
  toilets = Toilet.objects.all()
  cities = list(map(filter_cities, toilets))
  filtered_cities = list(set(cities))
  return render(request, 'toilets/wc_list.html', { 'toilets': toilets, 'cities': filtered_cities })