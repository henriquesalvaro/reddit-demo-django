"""
API V1: Comments Views
"""
###
# Libraries
###

from rest_framework import viewsets, permissions
from rest_framework.generics import get_object_or_404

from comments.models import Comment
from posts.models import Post
from topics.models import Topic
from .serializers import CommentSerializer
from topics.api.v1.permissions import IsOwnerOrReadOnly

###
# Filters
###


###
# Viewsets
###

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        topic = get_object_or_404(Topic, urlname=self.kwargs.get('topic_urlname'))
        post = get_object_or_404(Post, id=self.kwargs.get('post_pk'))
        serializer.save(author=self.request.user, post=post, topic=topic)

    def get_queryset(self):
        topic = get_object_or_404(Topic, urlname=self.kwargs.get('topic_urlname'))
        post = get_object_or_404(Post, id=self.kwargs.get('post_pk'))
        return Comment.objects.filter(topic=topic, post=post)
