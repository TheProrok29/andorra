from django.shortcuts import render


def statistics(request):
    context = {
        'character': request.character
    }
    return render(request, 'statistics.html', context)
