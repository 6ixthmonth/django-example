from django.db import models
from django.utils import timezone

from textwrap import shorten


class Board(models.Model):
    number = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=40)
    content = models.TextField(null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)
    user_id = models.CharField(max_length=20)
