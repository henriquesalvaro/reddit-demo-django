"""
Topics Models
"""
###
# Libraries
###
from django.db import models
from django.utils.text import slugify
from helpers.models import TimestampModel
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

class Topic(TimestampModel):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    urlname = models.SlugField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topics')

    class Meta:
        ordering = ('name',)

    def save(self, *args, **kwargs):
        self.urlname = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
