from django.urls import path

from . import views

urlpatterns = [
    path('', views.training_start, name='training_start'),
    path('training_active', views.training_active, name='training_active'),
    path('training_ending', views.training_ending, name='training_ending'),
]
