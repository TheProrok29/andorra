from datetime import timedelta

from django.http import HttpResponseServerError
from django.shortcuts import render, redirect
from django.views.generic.edit import View
from django.utils import timezone

from .definitions import JourneyDefinition, journey_list
from .models import ActiveJourney, toggle_journey_log_visibility, show_finished_journey_event_step


class JourneyView(View):

    def get(self, request):
        template_context = {}
        active_journey = ActiveJourney.objects.filter(character=request.character, active=True).first()
        last_journey = active_journey
        if last_journey is None:
            last_journey = ActiveJourney.objects.filter(character=request.character, active=False).first()
            definition: JourneyDefinition = next(filter(lambda j: j.slug == last_journey.slug, journey_list))
        definition: JourneyDefinition = next(filter(lambda j: j.slug == last_journey.slug, journey_list))
        last_journey_log = show_finished_journey_event_step(last_journey, timezone.now())
        template_context = {'journeys': journey_list,
                            'active_journey': active_journey,
                            'last_journey': last_journey,
                            'journey_disabled': request.character.busy,
                            'last_journey_name': definition.name,
                            'last_journey_log': last_journey_log}
        return render(request, 'journeys.html', template_context)

    def post(self, request):
        if 'journey_id' in request.POST:
            if len(ActiveJourney.objects.filter(character=request.character, active=True)) > 0:
                return HttpResponseServerError(status=500)
            ActiveJourney.objects.filter(character=request.character).delete()
            journey_id = request.POST['journey_id']
            definition: JourneyDefinition = next(filter(lambda j: j.slug == journey_id, journey_list))
            log = list(definition.proceed(request.character))
            duration = sum([l.duration for l in log])

            ActiveJourney(
                character=request.character,
                start_date=timezone.now(),
                end_date=timezone.now() + timedelta(seconds=duration),
                log=log,
                slug=journey_id,
            ).save()
        elif 'is_visible' in request.POST:
            last_journey = ActiveJourney.objects.filter(character=request.character, active=False).first()
            if last_journey is not None:
                toggle_journey_log_visibility(last_journey)
        return redirect('journeys')
