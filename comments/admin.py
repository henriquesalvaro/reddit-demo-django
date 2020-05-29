"""
Comments admin
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
@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'post', 'topic', 'author',)
