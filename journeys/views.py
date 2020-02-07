from datetime import timedelta


from django.http import HttpResponseServerError
from django.shortcuts import render, redirect
from django.views.generic.edit import View
from django.utils import timezone

from .definitions import JourneyDefinition, journey_list
from .models import ActiveJourney


class JourneyView(View):

    def get(self, request):
        active_journey = ActiveJourney.objects.filter(character=request.character, active=True).first()
        return render(request, 'journeys.html', {'journeys': journey_list,
                                                 'active_journey': active_journey,
                                                 'journey_disabled': request.character.busy,
                                                 })

    def post(self, request):
        if len(ActiveJourney.objects.filter(character=request.character, active=True)) > 0:
            return HttpResponseServerError(status=500)
        ActiveJourney.objects.filter(character=request.character).delete()
        journey_id = request.POST['journey_id']
        definition: JourneyDefinition = next(filter(lambda j: j.slug == journey_id, journey_list))
        log = list(definition.proceed(request.character))
        duration = sum([l.duration for l in log])

        ActiveJourney(
            character=request.character,
            end_date=timezone.now() + timedelta(seconds=duration),
            log=log
        ).save()
        return redirect('journeys')
