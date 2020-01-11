from django.shortcuts import render
from .models import Character


def statistics(request):
    kwargs = {}
    if(Character.objects.filter(pk=1).exists()):
        kwargs['character'] = Character.objects.get(pk=1)
    return render(request, 'statistics.html', kwargs)
