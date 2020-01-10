from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='journeys'),
    # path('journey-active', views.active, name='active'),
]
