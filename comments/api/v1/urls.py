"""
API V1: Comments Urls
"""
###
# Libraries
###
from django.conf.urls import url, include
from rest_framework_nested import routers

from comments.api.v1.views import CommentViewSet
from posts.api.v1.urls import topics_router

###
# Routers
###
""" Main router """
posts_router = routers.NestedSimpleRouter(topics_router, r'posts', lookup='post')
posts_router.register(r'comments', CommentViewSet, basename='comments')


###
# URLs
###
urlpatterns = [
    url(r'^', include(posts_router.urls)),
]
