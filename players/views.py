from django.shortcuts import render
from .models import Player


def statistics(request):
    kwargs = {}
    if(Player.objects.filter(pk=1).exists()):
        kwargs['player'] = Player.objects.get(pk=1)
    return render(request, 'statistics.html', kwargs)
