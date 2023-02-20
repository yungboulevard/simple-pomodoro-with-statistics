from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

import json
from .models import PomodoroModel

def home(request):
	return render(request, "users/index.html")


class PomodoroResultsTimeData(TemplateView):
	template_name = 'users/results.html'

	def get_results(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['user'] = self.request.user
		return context

def save_result(request):
	if request.method == 'POST':
		user_instance = User.objects.get(username=request.user)
		print(request.body)
		db_mins_plus_request_sec = (int(user_instance.pomodoromodel.pomodoro * 60) + (int(request.body)))
		print(db_mins_plus_request_sec)
		to_db_sec_to_mins = db_mins_plus_request_sec / 60
		print(to_db_sec_to_mins)
		user_instance.pomodoromodel.pomodoro = to_db_sec_to_mins
		user_instance.pomodoromodel.save()
		print(user_instance.pomodoromodel.pomodoro)


		return render(request, "users/index.html")


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"