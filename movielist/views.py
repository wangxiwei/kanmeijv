from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Movie


class IndexView(generic.ListView):
    model = Movie
    template_name = 'movielist/index.html'
    context_object_name = 'movie_list'


