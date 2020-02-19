from django.http import HttpRequest
from characters.models import Character


class UserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):

        if request.user.is_authenticated:
            character = Character.objects.filter(user=request.user).first()
            if character is not None:
                request.session['character_id'] = character.id
            elif request.character.user is None:
                request.character.user = request.user
                request.character.save()

        response = self.get_response(request)
        return response
