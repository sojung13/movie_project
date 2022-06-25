from django import urls


from django.urls import path
from . import views

app_name = ''
urlpatterns = [
    path('<str:movie_title>', views.vote),
    path('re/<str:movie_title>/<int:vote_id>', views.vote_ud),
    
]
 