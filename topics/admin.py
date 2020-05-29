"""
Topics admin
"""
###
# Libraries
###
from django.contrib import admin

from . import models


###
# Inline Admin Models
###


###
# Main Admin Models
###
@admin.register(models.Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title', 'urlname', 'description', 'author',)
