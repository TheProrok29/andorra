from django.shortcuts import render


def statistics(request):
    hero = request.character
    context = {
        'character': hero,
        'next_lvl': hero.next_level,
    }
    return render(request, 'statistics.html', context)
