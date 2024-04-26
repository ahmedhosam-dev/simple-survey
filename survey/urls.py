from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("", views.login, name="login"),
    path("survey", csrf_exempt(views.survey), name="survey"),
    path("add_survey", views.add_servey, name="add_survey"),
    path("thanks", views.thanks, name="thanks"),
    
]