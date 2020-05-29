"""
Comments URL Configuration
"""
###
# Libraries
###
from django.conf.urls import url, include


###
# URL Patterns
###
urlpatterns = [
    url(r'^', include('comments.api.v1.urls'))
]
