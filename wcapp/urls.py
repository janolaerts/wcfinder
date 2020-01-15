from django.contrib import admin
from django.urls import path, re_path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from toilets import views as toilets_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.citylist_view),
    path('toilet-list/', toilets_views.wclist_view),
    path('toilets/', include('toilets.urls')),
    path('add-toilet/', toilets_views.add_toilet_view),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)