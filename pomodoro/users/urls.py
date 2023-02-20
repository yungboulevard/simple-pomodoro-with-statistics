from django.urls import path
from . import views
urlpatterns = [

 path('home/', views.home, name = "home"),
 path('home/timedata/', views.PomodoroResultsTimeData.as_view(), name = "timedata"),
 path('home/saveresult/', views.save_result, name = "save_result"),
 path('signup/', views.SignUpView.as_view(), name= "signup"),

]