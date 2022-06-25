from rest_framework import serializers
from django.contrib.auth import get_user_model
from reviews.models import Review, Comment
from movies.models import Movie



class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('title',)




class ProfileSerializer(serializers.ModelSerializer):

    class ReviewSerializer(serializers.ModelSerializer):

        movie = MovieSerializer(read_only=True)


        class Meta:
            model = Review
            fields = ('content','movie')


    class CommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = ('content',)

    like_reviews = ReviewSerializer(many=True)
    like_movies = MovieSerializer(many=True)
    reviews = ReviewSerializer(many=True)
    comments = CommentSerializer(many=True)


    class Meta:
        model = get_user_model()
        fields = ('id', 'like_reviews', 'like_movies','followings', 'followers', 'username','reviews', 'comments')
