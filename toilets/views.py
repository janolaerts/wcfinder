from django.shortcuts import render, redirect
from . models import Toilet
from . import forms
from django.http import HttpResponse
import folium
from  geopy.geocoders import Nominatim

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

def map_view(request):
  # create map object
  map = folium.Map(location = [50.55, 4.50], zoom_start = 9)
  map.save('toilets/templates/toilets/map.html')

  # global tooltip
  toilets = Toilet.objects.all()

  # create markers
  for toilet in toilets:
    address = toilet.street, toilet.number, toilet.city
    geolocator = Nominatim()
    address = f'{ toilet.street } { toilet.number } { toilet.city }'
    location = geolocator.geocode(address)
    popupHtml = f'<div class="popup-wrapper"> <p>{ toilet.street } { toilet.number }, { toilet.city }</p> <p>Price: €{ toilet.price }</p> <p>Remarks: { toilet.remarks }</p> </div>'
    folium.Marker([location.latitude, location.longitude], popup=popupHtml, tooltip=f'{ toilet.street } { toilet.number }, { toilet.city }', icon=folium.Icon(color='red', icon='none')).add_to(map)

  return render(request, 'toilets/map_view.html', { 'map': map._repr_html_() })