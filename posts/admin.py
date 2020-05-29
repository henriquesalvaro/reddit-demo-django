"""
Posts admin
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
@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'topic', 'author',)
