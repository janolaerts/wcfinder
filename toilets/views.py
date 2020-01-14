from django.shortcuts import render
from . models import Toilet
from django.http import HttpResponse

# Create your views here.
def filter_cities(toilet):
  return toilet.city

#def filter_toilets(toilet, city):
  #if toilet.city == city:
    #return True

  #else:
    #return False

def wclist_view(request):
  toilet_list = Toilet.objects.all()
  cities = list(map(filter_cities, toilet_list))
  filtered_cities = list(set(cities))
  return render(request, 'toilets/wc_list.html', { 'toilets': toilet_list, 'cities': filtered_cities })