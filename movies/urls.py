from django.urls import path
from . import views

# /movies/title   GET POST

urlpatterns = [
    path("", views.Movies.as_view()),
    path("<str:title>/", views.MoviesDetail.as_view(), name='movie-detail'),
]