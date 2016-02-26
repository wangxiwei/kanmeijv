from django.contrib import admin
from .models import Movie


class MovieAdmin(admin.ModelAdmin):
    list_display = ('movie_name','movie_state','movie_update','movie_return','movie_countdown')
    list_filter = ['movie_update']
    search_fields = ['movie_name']

admin.site.register(Movie,MovieAdmin)