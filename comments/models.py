"""
Comments Models
"""
###
# Libraries
###

from django.db import models
from helpers.models import TimestampModel
from accounts.models import User
from posts.models import Post
from topics.models import Topic
###
# Choices
###


###
# Querysets
###


###
# Models
###


class Comment(TimestampModel):
    content = models.CharField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='comments')

    class Meta:
        ordering = ('created_at',)
