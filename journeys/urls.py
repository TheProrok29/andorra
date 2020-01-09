from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('journey-active', views.active, name='active'),
]
