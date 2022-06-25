from django.urls import path
from . import views

app_name = ''
urlpatterns = [
    # 영화 제목으로 검색
    path('search', views.movie_search),
    path('<str:movie_title>', views.movie_search_title),
    # 영화 연도, 장르로 검색
    path('search/genre/year', views.reco_genre_movie),
    # 기분으로 추천
    path('random/emotion', views.reco_emo_movie),
    # 영화 섞기
    path('double/shuffle', views.reco_double_movie),
    # 인기영화
    path('popular/movie', views.popular_movie),
    # 좋아요 누르기
    path('like/<int:movie_pk>', views.like_movie),
]
