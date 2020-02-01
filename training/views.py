from django.shortcuts import render, redirect
from datetime import datetime, timezone
from .models import Training


def training(request):
    hero = request.character
    training = request.training
    template_context = {
        'character': hero,
        'next_lvl': hero.next_level,
    }
    session_counter = count_number_of_sessions(training.start_training_date)
    if (request.method == 'GET') and (session_counter > 0):
        return redirect(training_active)
    if request.method == 'POST':
        hero.growth_points += session_counter
        hero.save()
        training = Training.objects.get(id=request.session['training_id'])
        training.delete()
        del request.session['training_id']
    return render(request, 'training.html', template_context)


def training_active(request):
    template_context = {}
    hero = request.character
    training = request.training

    session_counter = count_number_of_sessions(training.start_training_date)
    template_context['character'] = hero
    template_context['training'] = training
    template_context['session'] = session_counter
    template_context['next_lvl'] = hero.next_level,

    return render(request, 'training_active.html', template_context)


def count_number_of_sessions(training_start):
    time_now = datetime.now(timezone.utc)
    diff = time_now - training_start

    return diff.seconds // 20
