from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone

class University(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    website = models.URLField()

    def __str__(self):
        return str(self.name)

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)

    def _str_(self):
        return f"Review by {self.user.username} for {self.university.name}"