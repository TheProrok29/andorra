from django.shortcuts import render
from .models import ActiveJourney

journey_list = {
    'Easy': 'Kill the wolf',
    'Medium': 'Kill the wolf king',
    'Hard': 'Survive.'
}


def index(request):

    if request.method == 'POST':
        ActiveJourney(request.POST)

        finish_time = ActiveJourney.end_date.strftime('%Y-%m-%d %H:%M:%S')
        time_dict = {
            'Time finishing': finish_time
        }
        print(finish_time)
        return render(request, 'journey-active.html', {'dictionary': time_dict})

    else:
        return render(request, 'journeys.html', {'dictionary': journey_list})


# def active(request):
#
#     return render(request, 'journey-active.html', {'dictionary': journey_list})
