from django.shortcuts import render
from django.views.generic import TemplateView  # Import TemplateView
from django.http import JsonResponse
from django.core import serializers
from rest_framework import generics
from .serializers import MovieSerializer
from .models import MovieStore, MovieList, Comment
from rest_framework import permissions
from braces.views import LoginRequiredMixin
import json


# Create your views here.

class CreateView(generics.ListCreateAPIView):
    queryset = MovieStore.objects.all()
    serializer_class = MovieSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = MovieStore.objects.all()
    serializer_class = MovieSerializer


class IndexPageView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"
    queryset = MovieList.objects.all()
    serializer_class = MovieSerializer
    login_url = "/login/"

    def get(self, request, **kwargs):

        movies = MovieStore.objects.all()
        moviesJson = json.loads(serializers.serialize('json', movies))
        mylist = MovieList.objects.all().filter(owner=request.user)
        mylistJson = json.loads(serializers.serialize('json', mylist))

        comments = Comment.objects.all().filter(owner=request.user)
        commentsJson = json.loads(serializers.serialize('json', comments))

        # movie = MovieStore.objects.all().filter(name="Poltergeist")
        # print(json.loads(serializers.serialize('json', movie)))
        # print(json.loads(serializers.serialize(
        #     'json', movie.get().comments.all())))

        context = {
            'movies': moviesJson,
            'mylist': mylistJson,
            'comments': commentsJson
        }

    #    print(commentsJson)
        return render(request, 'index.html', context)

    def post(self, request, **kwargs):
       # print(request.POST['movie_name'])
        if 'movie_name' in request.POST:
            movie_name = request.POST['movie_name']
            mylistnew = MovieList(movie=MovieStore.objects.get(
                name=movie_name), owner=request.user)
            mylistnew.save()
        if 'comment' in request.POST:
            comment = Comment(comment=request.POST['comment'], movie=MovieStore.objects.get(
                pk=request.POST['movie_comment']), owner=request.user)
            comment.save()
        movies = MovieStore.objects.all()
        moviesJson = json.loads(serializers.serialize('json', movies))
        mylist = MovieList.objects.all().filter(owner=request.user)
        mylistJson = json.loads(serializers.serialize('json', mylist))

        comments = Comment.objects.all().filter(owner=request.user)
        commentsJson = json.loads(serializers.serialize('json', comments))

       # print(commentsJson)

        # movie = MovieStore.objects.all().filter(name="Poltergeist")
        # print(json.loads(serializers.serialize('json', movie)))
        # print(json.loads(serializers.serialize(
        #     'json', movie.get().comments.all())))

        context = {
            'movies': moviesJson,
            'mylist': mylistJson,
            'comments': commentsJson
        }
        return render(request, 'index.html', context)
