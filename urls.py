from django.contrib import admin
from django.urls import include, path
from django.urls import url
urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns += [
    path('catalog/', include('catalog.urls')),
]
