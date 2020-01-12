from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from toilets import views as toilets_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', toilets_views.wclist_view),
    path('toilets/', include('toilets.urls')),
]

urlpatterns += staticfiles_urlpatterns()