from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Movie,HDTV


class IndexView(generic.ListView):
    model = Movie
    template_name = 'movielist/index.html'
    context_object_name = 'movie_list'


class HDTVView(generic.ListView):
    model = HDTV
    template_name = 'movielist/hdtv.html'
    context_object_name = 'HDTV_list'
