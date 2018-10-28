from .views import *
#from . import url_converters
from django.urls import register_converter, path
app_name =  "main"
urlpatterns = [

    path('ping',ping),
    path('goals/new/',GoalView.as_view()),
]