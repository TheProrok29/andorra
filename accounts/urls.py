from django.urls import path
from . import views
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('password/', PasswordChangeView.as_view(template_name='registration/password_change.html',
                                                 success_url=reverse_lazy('home')), name='PasswordChange'),
]
