from django.urls import path
from .views import *

urlpatterns = [
    path("", MainView, name="index"),
    path("students",CreateStudentView, name="create_student")
]