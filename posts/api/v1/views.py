"""
API V1: Posts Views
"""
###
# Libraries
###
from rest_framework import viewsets, permissions
from rest_framework.generics import get_object_or_404

from topics.models import Topic
from .serializers import PostSerializer
from posts.models import Post
from topics.api.v1.permissions import IsOwnerOrReadOnly
###
# Filters
###


###
# Viewsets
###


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        topic = get_object_or_404(Topic, urlname=self.kwargs.get('topic_urlname'))
        serializer.save(author=self.request.user, topic=topic)

    def get_queryset(self):
        topic = get_object_or_404(Topic, urlname=self.kwargs.get('topic_urlname'))
        return Post.objects.filter(topic=topic)
