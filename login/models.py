from django.db import models
from django.utils import timezone

# Create your models here.
class Route(models.Model):
    driver = models.ForeignKey('auth.User')
    start_location = models.CharField(max_length=200)
    end_location = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)