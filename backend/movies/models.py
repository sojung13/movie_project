from django.db import models
from django.conf import settings


class Genre(models.Model):
    name = models.CharField(max_length=20)






class Movie(models.Model):
    title = models.CharField(max_length=100)
    poster_path = models.TextField(blank=True, null=True)
    overview = models.TextField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    vote_average = models.FloatField(blank=True, null=True)
    backdrop_path = models.TextField(blank=True, null=True)
    genre_ids = models.ManyToManyField(Genre, related_name='movies', blank=True)
    # 좋아요 누른 유저
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    popularity = models.FloatField(blank=True, null=True)

    
