from rest_framework import serializers
from votes.models import Vote
from .models import Movie, Genre
from reviews.serializers.review import ReviewListSerializer

class MovieSerializer(serializers.ModelSerializer):

    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('name','pk')
    
    class VoteSerializer(serializers.ModelSerializer):
        class Meta:
            model = Vote
            fields = '__all__'


    genre_ids = GenreSerializer(many=True)
    reviews = ReviewListSerializer(many=True)
    votes = VoteSerializer(many=True)


    class Meta:
        model = Movie
        fields = ('id','genre_ids', 'title', 'overview', 
        'poster_path', 'release_date','vote_average','backdrop_path',
        'like_users','reviews','votes',)

