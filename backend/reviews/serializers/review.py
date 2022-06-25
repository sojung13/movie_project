from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import Review, Comment
from .comments import CommentSerializer


User = get_user_model()


class ReviewListSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')



    comments = CommentSerializer(read_only=True, many=True)
    user = UserSerializer(read_only=True)
    like_users = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Review
        fields = ('pk', 'user','like_users','content','movie','comments','created_at','updated_at')

class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('content',)