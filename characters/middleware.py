import os
import random
from math import floor

from django.http import HttpRequest

from .models import Character

names = []
with open(os.path.join(os.path.dirname(__file__), 'names.txt'), encoding='utf8') as file:
    names = [line.strip() for line in file.readlines()]


class CharacterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        request.character = Character.objects.get(id=request.session['character_id'])
        response = self.get_response(request)

        return response


class InceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        if 'character_id' not in request.session:
            new_character = Character()
            new_character.name = random.choice(names)
            new_character.level = 10
            new_character.health_points = 10
            new_character.force = 3
            new_character.save()
            request.session['character_id'] = new_character.id

        response = self.get_response(request)

        return response


class LevelingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        character: Character = request.character
        while (character.level < 100 and character.skill_points > floor(6 * (1.1 ** character.level))):
            character.level += 1
            character.health_points = character.level
            character.force = floor(character.level / 3)
            character.save()

        response = self.get_response(request)

        return response
