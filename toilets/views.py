from django.shortcuts import render
from . models import Toilet

# Create your views here.
def wclist_view(request):
  toilets = Toilet.objects.all()
  return render(request, 'toilets/wc_list.html', { 'toilets': toilets })