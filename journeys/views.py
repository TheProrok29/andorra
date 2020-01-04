from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = 'number of books'
    num_instances = 'blabla'

    # Available books (status = 'a')
    num_instances_available = 'bla'

    # The 'all()' is implied by default.
    num_authors = 'bla'

    my_dictionary = {
        "Easy": "Kill the wolf",
        "Medium": "Kill the wolf king",
        "Hard": "Survive."
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'journeys.html', {'dictionary': my_dictionary})
