from django.http import HttpRequest

from .models import Training


class TrainingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        if 'training_id' not in request.session:
            new_training = Training()
            new_training.save()
            request.session['training_id'] = new_training.id

        request.training = Training.objects.get(id=request.session['training_id'])
        response = self.get_response(request)

        return response
