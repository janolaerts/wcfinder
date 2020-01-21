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
  toiletList = list(Toilet.objects.filter(city=city))

  for toilet in toiletList:
    geolocator = Nominatim()
    address = f'{ toilet.street } { toilet.number } { toilet.city }'
    location = geolocator.geocode(address)

    map = folium.Map(location = [location.latitude, location.longitude], zoom_start = 20, width = '100%', height = '100%', control_scale = False, zoom_control = False)
    icon = folium.Icon(color='red', icon='none')
    folium.Marker([location.latitude, location.longitude], icon = icon).add_to(map)

    toilet.map = map._repr_html_()

  return render(request, 'toilets/wc_list.html', { 'toilets': toiletList })

def add_toilet_view(request):
  form = forms.AddToilet(request.POST)

  if request.method == 'POST':
    if form.is_valid():
      toilet = form.save()
      return render(request, 'toilets/toilet_added.html', { 'toilet': toilet })
      
  return render(request, 'toilets/add_toilet.html', { 'form': form })

def edit_toilet_view(request):
  form = forms.EditToilet(request.POST)
  toilet = request.GET.get('toilet')
  id = request.GET.get('id')

  toiletToUpdate = Toilet.objects.filter(id = id)
  print(toiletToUpdate)
  
  if request.method == 'POST':
    if form.is_valid():
      city = request.POST.get('city')
      street = request.POST.get('street')
      number = request.POST.get('number')
      cleaned = request.POST.get('cleaned')
      wheelchair_accessible = request.POST.get('wheelchair_accessible')

      toiletToUpdate.update(city = city, street = street, number = number, cleaned = cleaned, wheelchair_accessible = wheelchair_accessible)

  return render(request, 'toilets/edit_toilet.html', { 'form': form })

def delete_toilet_view(request):
  id = request.GET.get('id')
  Toilet.objects.filter(id=id).delete()

  city = request.GET.get('city')
  toilet_list = Toilet.objects.filter(city=city)
  return render(request, 'toilets/wc_list.html', { 'toilets': toilet_list })

def map_view(request):
  # create map object
  map = folium.Map(location = [50.55, 4.50], zoom_start = 7, width = '100%', height = '100%', control_scale = True, zoom_control = False)
  map.save('toilets/templates/toilets/map.html')

  toilets = Toilet.objects.all()

  for toilet in toilets:
    address = toilet.street, toilet.number, toilet.city
    geolocator = Nominatim()
    address = f'{ toilet.street } { toilet.number } { toilet.city }'
    location = geolocator.geocode(address)

    icon = folium.Icon(color='red', icon='none')
    popup = folium.Popup(html = f'<div class="popup-wrapper"> <h4>Location: { toilet.street } { toilet.number }, { toilet.city }</h4> <p>Price: €{ toilet.price }</p> <p>Clean: { toilet.cleaned }</p> <p>Wheelchair: { toilet.wheelchair_accessible }</p> </div>', max_width = 200, min_width = 200)
    tooltip = f'{ toilet.street } { toilet.number }, { toilet.city }'

    folium.Marker([location.latitude, location.longitude], popup = popup, tooltip = tooltip, icon = icon).add_to(map)

  return render(request, 'toilets/map_view.html', { 'map': map._repr_html_() })