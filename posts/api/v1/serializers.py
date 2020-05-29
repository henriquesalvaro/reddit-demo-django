"""
API V1: Posts Serializers
"""
###
# Libraries
###
from rest_framework import serializers
from posts.models import Post
from rest_auth.serializers import UserDetailsSerializer
from topics.api.v1.serializers import TopicDetailSerializer
###
# Serializers
###


class PostSerializer(serializers.ModelSerializer):
    author = UserDetailsSerializer(read_only=True)
    topic = TopicDetailSerializer(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('author','topic',)


class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title','author', 'created_at',)
