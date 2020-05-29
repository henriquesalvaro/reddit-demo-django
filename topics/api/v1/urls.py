"""
API V1: Topics Urls
"""
###
# Libraries
###
from django.conf.urls import url, include
from rest_framework_nested import routers
from . import views

###
# Routers
###
""" Main router """
router = routers.SimpleRouter()
router.register(r'topics', views.TopicViewSet, basename='topics')

###
# URLs
###
urlpatterns = [
    url(r'^', include(router.urls)),
]
