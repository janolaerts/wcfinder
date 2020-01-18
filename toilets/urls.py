from django.urls import path
from . import views

app_name = 'toilets'

urlpatterns = [
  path('toilet-list/', views.wclist_view),
  path('add-toilet/', views.add_toilet_view),
  path('delete-toilet/', views.delete_toilet_view)
]