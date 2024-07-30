from django.urls import path
from . import views

# /students/code   GET POST

urlpatterns = [
    path("", views.Students.as_view()),
    path("<str:code>/", views.StudentDetail.as_view())
]