import logging

from django.core.management import BaseCommand
from django.utils import timezone

from topics.models import Topic
from posts.models import Post
from comments.models import Comment

logger = logging.getLogger('amazon-logs')


class Command(BaseCommand):

    def handle(self, *args, **options):
        logger.info({'action': 'START_HOURLY_SUMMARY'})
        last_hour = timezone.now() - timezone.timedelta(hours=1)
        summary = {
            'topic': Topic.objects.filter(created_at__gte=last_hour).count(),
            'posts': Post.objects.filter(created_at__gte=last_hour).count(),
            'comments': Comment.objects.filter(created_at__gte=last_hour).count(),
        }
        logger.info({'action': 'HOURLY_ACTIVITY_SUMMARY', 'summary': summary})
        logger.info({'action': 'FINISH_HOURLY_SUMMARY'})
