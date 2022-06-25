from django.contrib import admin
from django.contrib.auth import get_user_model
from movies.models import Movie,Genre
from reviews.models import Review,Comment
from votes.models import Vote

# Register your models here.
admin.site.register(get_user_model())
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Review)
admin.site.register(Comment)
admin.site.register(Vote)
