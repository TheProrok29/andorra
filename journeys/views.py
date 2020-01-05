from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import Context, loader


def index(request):
    """View function for home page of site."""

    journey_list = {
        'Easy': 'Kill the wolf',
        'Medium': 'Kill the wolf king',
        'Hard': 'Survive.'
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'journeys.html', {'dictionary': journey_list})
