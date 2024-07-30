from django.shortcuts import render
from rest_framework.views import APIView
from .models import Movie
from .serializers import MoviesSerializer
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_204_NO_CONTENT
from urllib.parse import unquote

# Create your views here.
class Movies(APIView):

    def get(self, request):
        all_movies = Movie.objects.all()
        serializer = MoviesSerializer(all_movies, many=True)
        return Response(serializer.data)

        
    def post(self, request):
        movie = MoviesSerializer(data=request.data)
        if movie.is_valid():
            movie.save()
            return Response(movie.data)
        else:
            return Response(movie.errors)
        

class MoviesDetail(APIView):
    def get_object(self, title):
        decoded_title = unquote(title)
        try:
            movie = Movie.objects.get(title=decoded_title)
        except:
            raise NotFound
        return movie
    
    def get(self, request, title):
        movie = self.get_object(title)
        serializer = MoviesSerializer(movie)
        return Response(serializer.data)

    def put(self, request, title):
        movie = self.get_object(title)
        serializer = MoviesSerializer(movie, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


    def delete(self, request, title):
        movie = self.get_object(title)
        movie.delete()
        return Response(status=HTTP_204_NO_CONTENT)