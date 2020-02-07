from django.shortcuts import render, redirect
from datetime import datetime, timezone
from .models import Training, start_trainning, stop_training
from datetime import timedelta
from django.views import View


class TrainingStart(View):
    def render_training(self, request):
        hero = request.character
        # print(hero.busy)
        template_context = {
            'training_disabled': hero.busy,
            'character': hero,
            'next_lvl': hero.next_level
        }
        return render(request, 'training.html', template_context)

    def get(self, request):
        hero = request.character
        training = Training.objects.filter(character=hero).first()
        if training is not None:
            if training.is_ending:
                print(training.is_ending)
                return redirect(training_ending)
            else:
                return redirect(training_active)
        return self.render_training(request)

    def post(self, request):
        hero = request.character
        if(hero.busy):
            training = Training.objects.filter(character=hero).first()
            hero.growth_points += training.number_completed_training + 1
            hero.save()
            stop_training(hero)
        return self.render_training(request)


class TrainingActive(View):
    def render_training_active(self, request):
        hero = request.character
        training = Training.objects.filter(character=hero).first()
        training_done_counter, actual_training_rest = count_number_of_trainings(training.start_training_date)
        template_context = {
            'character': hero,
            'training': training,
            'training_done_counter': training_done_counter,
            'actual_training_rest': actual_training_rest,
            'next_lvl': hero.next_level,
        }
        return render(request, 'training_active.html', template_context)

    def get(self, request):
        hero = request.character
        if hero.busy:
            return self.render_training_active(request)

    def post(self, request):
        hero = request.character
        if not hero.busy:
            start_trainning(hero)
        return self.render_training_active(request)


class TrainingEnding(View):
    def render_training_ending(self, request):
        hero = request.character
        training = Training.objects.filter(character=hero).first()
        training_done_counter, actual_training_rest = count_number_of_trainings(training.start_training_date)
        template_context = {
            'character': hero,
            'training': training,
            'training_done_counter': training_done_counter,
            'actual_training_rest': actual_training_rest,
            'next_lvl': hero.next_level,
            'ending': training.end_training_date,
            'time_now': datetime.now(timezone.utc)
        }
        return render(request, 'training_ending.html', template_context)

    def get(self, request):
        return self.render_training_ending(request)

    def post(self, request):
        hero = request.character
        training = Training.objects.filter(character=hero).first()
        training_done_counter, actual_training_rest = count_number_of_trainings(training.start_training_date)

        if not training.is_ending:
            training.end_training_date = datetime.now(timezone.utc) + timedelta(seconds=20)
            training.is_ending = True
            training.number_completed_training = training_done_counter
            training.save()
        return self.render_training_ending(request)


training_start = TrainingStart.as_view()
training_active = TrainingActive.as_view()
training_ending = TrainingEnding.as_view()


def count_number_of_trainings(training_start):
    time_now = datetime.now(timezone.utc)
    diff = time_now - training_start
    return diff.seconds // 20, diff.seconds % 20
