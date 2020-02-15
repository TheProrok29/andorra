from django.http import HttpRequest


class UserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):

        if request.user.is_authenticated and request.character.user == None:
            request.character.user = request.user
            request.character.save()

        response = self.get_response(request)
        return response
