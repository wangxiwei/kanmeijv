# encoding=utf-8
from __future__ import unicode_literals

from django.db import models


class Movie(models.Model):
    movie_name = models.CharField(max_length=500)
    movie_url = models.CharField(max_length=1000)
    movie_state = models.CharField(max_length=50)
    movie_update = models.CharField(max_length=50)
    movie_return = models.CharField(max_length=50)
    movie_countdown = models.CharField(max_length=50)

    def __unicode__(self):
        return self.movie_name
