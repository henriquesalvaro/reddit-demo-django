"""
API V1: Topics Views
"""
###
# Libraries
###
from rest_framework import viewsets, permissions

from .serializers import TopicSerializer
from .permissions import IsOwnerOrReadOnly
from topics.models import Topic


###
# Viewsets
###

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    lookup_field = 'urlname'

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
