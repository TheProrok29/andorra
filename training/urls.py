from django.urls import path

from . import views

urlpatterns = [
    path('', views.training, name='training'),
    path('training_active', views.training_active, name='training_active'),
]
