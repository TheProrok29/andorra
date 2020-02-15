from dataclasses import dataclass
from django.shortcuts import render


@dataclass
class Achievement:
    name: str
    description: str


def achievements(request):
    character_achievements = []
    if request.character.growth_points >= 1:
        character_achievements.append(Achievement('TEST', 'Your first achievement!'))
    if request.character.health_points > 50:
        character_achievements.append(Achievement('Long life', 'You will live long.'))
    if request.character.strength > 10 and request.character.defense_strength > 5:
        character_achievements.append(Achievement('Powerful', 'You are a warrior.'))

    return render(request, 'achievements.html', {'achievements': character_achievements})
