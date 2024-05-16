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

class SavedUniversity(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'university')

    def _str_(self):
        return f"{self.user.username}'s saved university: {self.university.name}"
