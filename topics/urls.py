"""
Topics URL Configuration
"""
###
# Libraries
###
from django.conf.urls import url, include


###
# URL Patterns
###
urlpatterns = [
    url(r'^', include('topics.api.v1.urls'))
]
