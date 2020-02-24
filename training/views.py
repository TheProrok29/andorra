from django.views import View
from django.shortcuts import render, redirect
from datetime import datetime, timezone
from .models import Training, create_trainning, delete_training, set_is_ending_training
from .models import count_number_of_trainings, add_training_points_to_character


class TrainingView(View):
    def render_training(self, request):
        template_context = {
            'character': request.character,
        }
        return render(request, 'training.html', template_context)

    def render_training_active(self, request):
        training = Training.objects.filter(character=request.character).first()
        training_done_counter, actual_training_rest = count_number_of_trainings(training)
        template_context = {
            'character': request.character,
            'training': training,
            'training_done_counter': training_done_counter,
            'actual_training_rest': actual_training_rest,
        }
        return render(request, 'training_active.html', template_context)

    def render_training_ending(self, request):
        training = Training.objects.filter(character=request.character).first()
        training_done_counter, actual_training_rest = count_number_of_trainings(training)
        template_context = {
            'character': request.character,
            'training': training,
            'training_done_counter': training_done_counter,
            'actual_training_rest': actual_training_rest,
            'ending': training.end_training_date,
            'time_now': datetime.now(timezone.utc)
        }
        return render(request, 'training_ending.html', template_context)

    def get(self, request):
        training = Training.objects.filter(character=request.character).first()
        if training is not None:
            if training.is_ending:
                return self.render_training_ending(request)
            else:
                return self.render_training_active(request)
        return self.render_training(request)


class TrainingStart(TrainingView):
    def post(self, request):
        add_training_points_to_character(request.character)
        delete_training(request.character)
        return redirect(training_start)


class TrainingActive(TrainingView):
    def post(self, request):
        if not request.character.busy:
            create_trainning(request.character)
        return redirect(training_active)


class TrainingEnding(TrainingView):
    def post(self, request):
        training = Training.objects.filter(character=request.character).first()
        if not training.is_ending:
            set_is_ending_training(training)
        return redirect(training_ending)


training_start = TrainingStart.as_view()
training_active = TrainingActive.as_view()
training_ending = TrainingEnding.as_view()
