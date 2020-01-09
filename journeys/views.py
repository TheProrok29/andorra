from django.shortcuts import render

journey_list = {
    'Easy': 'Kill the wolf',
    'Medium': 'Kill the wolf king',
    'Hard': 'Survive.'
}


def index(request):

    return render(request, 'journeys.html', {'dictionary': journey_list})


def active(request):

    return render(request, 'journey-active.html', {'dictionary': journey_list})
