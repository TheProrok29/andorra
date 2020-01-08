from django.shortcuts import render
from .models import Player


def statistics(request):
    kwargs = {}
    kwargs['player'] = Player.objects.get(pk=1)
    return render(request, 'statistics.html', kwargs)
