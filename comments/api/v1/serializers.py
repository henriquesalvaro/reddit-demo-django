"""
API V1: Comments Serializers
"""
###
# Libraries
###

from rest_framework import serializers
from comments.models import Comment
from rest_auth.serializers import UserDetailsSerializer

from posts.api.v1.serializers import PostDetailSerializer
from topics.api.v1.serializers import TopicDetailSerializer

###
# Serializers
###


class CommentSerializer(serializers.ModelSerializer):
    author = UserDetailsSerializer(read_only=True)
    topic = TopicDetailSerializer(read_only=True)
    post = PostDetailSerializer(read_only = True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('author', 'topic', 'post',)
