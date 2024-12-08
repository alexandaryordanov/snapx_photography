from django.db import models
from django.db.models import Count


class CategoryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().annotate(contest_count=Count('contest')).order_by('-contest_count')
