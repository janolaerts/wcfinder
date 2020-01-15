from django.shortcuts import render
from . models import Toilet

# Create your views here.
def filter_cities(toilet):
  return toilet.city

#def filter_toilets(toilet, city):
  #if toilet.city == city:
    #return True

  #else:
    #return False

def wclist_view(request):
  city = request.GET.get('city')
  toilet_list = Toilet.objects.filter(city=city)
  return render(request, 'toilets/wc_list.html', { 'toilets': toilet_list})