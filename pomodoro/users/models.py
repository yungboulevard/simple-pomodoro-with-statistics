from django.db import models
from annoying.fields import AutoOneToOneField
from django.contrib.auth.models import User



class PomodoroModel(models.Model):
	user = AutoOneToOneField(User, primary_key=True, on_delete=models.CASCADE)
	pomodoro = models.DecimalField(max_digits=10, decimal_places=2)


	def __str__(self):
		return f'{self.user} {self.pomodoro}'

