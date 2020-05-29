"""
Posts Models
"""
###
# Libraries
###
from django.db import models
from helpers.models import TimestampModel
from topics.models import Topic
from accounts.models import User

###
# Choices
###


###
# Querysets
###


###
# Models
###

class Post(TimestampModel):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='posts')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('created_at',)
