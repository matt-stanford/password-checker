from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('password_check/', views.password_check, name='password_check'),
    path('password_generator/', views.password_generator, name='password_generator'),
]