from django.db import models
from django.conf import settings
from movies.models import Movie
# Create your models here.
class Vote(models.Model):
    rate = models.FloatField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='votes')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='votes')