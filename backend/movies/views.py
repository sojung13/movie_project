from pprint import pprint
from .models import Movie
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MovieSerializer
from django.db.models import Q
import random
from django.shortcuts import get_object_or_404
from django.db.models import Count


# 인기영화 
@api_view(['GET'])
def popular_movie(request):
    popular = Movie.objects.all().order_by('-popularity')[:24]
    serializer = MovieSerializer(popular, many=True)
    return Response(serializer.data)





# 영화제목으로 검색
# 1. 연관 검색어 관련단어 포함 모두 리턴해줌
@api_view(['GET'])
def movie_search(request):
    search_keyword = request.GET.get('search_keyword')
    if search_keyword :
        movie_list = Movie.objects.filter(title__icontains=search_keyword)[:5]
        serializer = MovieSerializer(movie_list, many=True)
        return Response(serializer.data)

#2. 제목으로 리턴
@api_view(['GET'])
def movie_search_title(request,movie_title):
    movie = Movie.objects.filter(title=movie_title)[0]
    # movie = Movie.objects.annotate(
    #     like_count=Count('like_users', distinct=True),
    #     title=movie_title)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)



# 장르 아이디 or 연도로 검색
# 조건에 맞는 영화 중 24개를 랜덤으로 보여줌
@api_view(['GET'])
def reco_genre_movie(request):
    genres = request.GET.get('genres')
    search_year = request.GET.get('year')
    if genres and search_year:
        movie_list = Movie.objects.filter(Q(genre_ids=genres) & Q(release_date__year = search_year))
        serializer = MovieSerializer(movie_list, many=True)
        return Response(serializer.data)
    elif not genres and search_year:
        movie_list = Movie.objects.filter(release_date__year = search_year)
        serializer = MovieSerializer(movie_list, many=True)
        return Response(serializer.data)



# 기분에 따른 장르 추천
@api_view(['GET'])
def reco_emo_movie(request):
    emotion = request.GET.get('emotion')
    if emotion == '설레고 싶어요':
        # 코미디, 로맨스, 모험
        movie_list = Movie.objects.filter(Q(genre_ids=35) | Q(genre_ids=10749) | Q(genre_ids=12))
        movie_list = random.sample(list(movie_list), 24)
    elif emotion == '우울해요':
        # 음악, 애니메이션, 판타지
        movie_list = Movie.objects.filter(Q(genre_ids=10402) | Q(genre_ids=16) | Q(genre_ids=14))
        movie_list = random.sample(list(movie_list), 24)
    elif emotion == '지루해요':
        #액션, 범죄, 미스터리, 전쟁
        movie_list = Movie.objects.filter(Q(genre_ids=28) | Q(genre_ids=80) | Q(genre_ids=9648) | Q(genre_ids=10752))
        movie_list = random.sample(list(movie_list), 24)
    elif emotion == '울고 싶어요':
        #가족, 드라마, TV영화
        movie_list = Movie.objects.filter(Q(genre_ids=10751) | Q(genre_ids=18) | Q(genre_ids=10770))
        movie_list = random.sample(list(movie_list), 24)
    elif emotion == '놀라고 싶어요':
        #공포, SF, 스릴러
        movie_list = Movie.objects.filter(Q(genre_ids=27) | Q(genre_ids=878) | Q(genre_ids=53))
        movie_list = random.sample(list(movie_list), 24)
    elif emotion == '자고 싶어요':
        #역사, 다큐멘터리, 서부
        movie_list = Movie.objects.filter(Q(genre_ids=36) | Q(genre_ids=99) | Q(genre_ids=37))
        movie_list = random.sample(list(movie_list), 24)

    serializer = MovieSerializer(movie_list, many=True)
    return Response(serializer.data) 


# 영화 2개 섞어서 추천하기
@api_view(['GET'])
def reco_double_movie(request):
    pprint(request.GET.get('genres'))
    # 리스트로 보낼것
    genres = request.GET.get('genres')
    genres = list(map(int, genres.strip('[]').split(',')))
    pick1, pick2 = random.sample(genres, 2)
    movie_list = list(Movie.objects.filter(Q(genre_ids=pick1) | Q(genre_ids=pick2)))
    movie_list = random.sample(list(movie_list),24)
    serializer = MovieSerializer(movie_list, many=True)
    return Response(serializer.data) 


@api_view(['POST'])
# 영화 좋아요 누르기
def like_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    # 이미 좋아요 눌렀으면 좋아요 취소
    if movie.like_users.filter(pk=request.user.pk).exists():
        movie.like_users.remove(request.user)
    else:
        movie.like_users.add(request.user)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)
    