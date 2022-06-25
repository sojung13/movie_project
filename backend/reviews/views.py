from django.shortcuts import get_object_or_404
from .models import Review, Comment
from movies.models import Movie
from django.contrib.auth import get_user_model
from .serializers.review import ReviewListSerializer, ReviewCreateSerializer
from .serializers.comments import CommentSerializer, CommentCreateSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from movies.serializers import MovieSerializer


User = get_user_model()


@api_view(['GET','POST']) 
def review_cr(request, movie_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)
    movie_serializer = MovieSerializer(movie)
    if request.method == 'GET':
        reviews = Review.objects.filter(movie=movie_pk)
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(movie_serializer.data)
    elif request.method == 'POST':
        serializer = ReviewCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=user)
            return Response(movie_serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT','DELETE'])
def review_ud(request, review_pk):
    user = request.user
    movie_pk = request.data['movie']
    movie = get_object_or_404(Movie, pk=int(movie_pk))
    movie_serializer = MovieSerializer(movie)
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'DELETE':
        if user == review.user:
            review.delete()
            return Response(movie_serializer.data)
    # 얘도 영화정보를 리턴해주고 바로 state변경처리 해줘야함
    elif request.method == 'PUT':
        if user == review.user:
            serializer = ReviewCreateSerializer(instance=review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(movie_serializer.data)


@api_view(['GET','POST'])
def comment_cr(request, review_pk):
    user = request.user
    movie_pk = request.data['movie']
    movie = get_object_or_404(Movie, pk=int(movie_pk))
    movie_serializer = MovieSerializer(movie)
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        comments = Comment.objects.filter(review=review_pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(movie_serializer.data)
    elif request.method == 'POST':
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(review=review, user=user)
            return Response(movie_serializer.data)


@api_view(['PUT','DELETE'])
def comment_ud(request, comment_pk):
    user = request.user
    movie_pk = request.data['movie']
    movie = get_object_or_404(Movie, pk=int(movie_pk))
    movie_serializer = MovieSerializer(movie)
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'DELETE':
        if user == comment.user:
            comment.delete()
            return Response(movie_serializer.data)
    elif request.method == 'PUT':
        if user == comment.user:
            serializer = ReviewCreateSerializer(instance=comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(movie_serializer.data)

@api_view(['POST',])
def review_like(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    # 이미 좋아요 눌렀으면 좋아요 취소
    if review.like_users.filter(pk=request.user.pk).exists():
        review.like_users.remove(request.user)
    else:
        review.like_users.add(request.user)
    serializer = ReviewListSerializer(review)
    return Response(serializer.data)


@api_view(['POST',])
def comment_like(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    # 이미 좋아요 눌렀으면 좋아요 취소
    if comment.like_users.filter(pk=request.user.pk).exists():
        comment.like_users.remove(request.user)
    else:
        comment.like_users.add(request.user)
    serializer = CommentSerializer(comment)
    return Response(serializer.data)





