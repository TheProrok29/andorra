from django.urls import path

from . import views


urlpatterns = [
    path('', views.JourneyView.as_view(), name='journeys'),
]
