from .forms import SignUpForm
from django.views import generic
from django.urls import reverse_lazy


class SignUp(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
