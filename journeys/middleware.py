from django.http import HttpRequest
from django.utils import timezone
from training.models import Training

from .models import ActiveJourney


class JourneysMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        active_journey = ActiveJourney.objects.filter(character=request.character, active=True).first()
        if active_journey is not None:
            request.character.busy = True
            request.character.save()
        if active_journey and timezone.now() > active_journey.end_date:
            active_journey.active = False
            if Training.objects.filter(character=request.character).first() is None:
                request.character.busy = False
                request.character.save()
            active_journey.save()

        response = self.get_response(request)

        return response
