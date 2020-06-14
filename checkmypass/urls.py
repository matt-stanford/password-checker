from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('checks.urls')),
    path('admin/', admin.site.urls),
]
