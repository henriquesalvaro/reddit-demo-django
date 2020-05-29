"""
API V1: Posts Urls
"""
###
# Libraries
###
from django.conf.urls import url, include
from rest_framework_nested import routers
from .views import PostViewSet
from topics.api.v1.urls import router

###
# Routers
###
""" Main router """
topics_router = routers.NestedSimpleRouter(router, r'topics', lookup='topic')
topics_router.register(r'posts', PostViewSet, basename='topic-posts')


###
# URLs
###
urlpatterns = [
    url(r'^', include(topics_router.urls)),
]
