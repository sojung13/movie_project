from pprint import pprint
from django.shortcuts import render
from rest_framework.decorators import api_view
from movies.serializers import MovieSerializer
from movies.models import Movie
from django.shortcuts import get_object_or_404
from .serializers import VoteSerializer
from rest_framework.response import Response
from .models import Vote
from votes import serializers



# 평점 주면 영화데이터를 넘겨줘야겠지?
@api_view(['POST'])
def vote(request, movie_title):
    movie = Movie.objects.filter(title=movie_title)[0]

    movie_serializer = MovieSerializer(movie)
    serializer = VoteSerializer(data=request.data)
    #이미 있다면 그냥 저장 안함
    if movie.votes.filter(user=request.user.pk).exists():
        return Response(movie_serializer.data)
    # 없을 때만 저장
    else:
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(movie_serializer.data)


@api_view(['PUT','DELETE'])
def vote_ud(request,movie_title,vote_id):
    movie = Movie.objects.filter(title=movie_title)[0]
    movie_serializer = MovieSerializer(movie)
    vote = get_object_or_404(Vote, pk=vote_id)
    if request.method == 'PUT':
        serializer = VoteSerializer(instance=vote, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(movie_serializer.data)
    elif request.method == 'DELETE':
        vote.delete()
        return Response(movie_serializer.data)
