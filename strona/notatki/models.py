from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'roboczy', 'Roboczy'
        PUBLISHED = 'opublikowany', 'Opublikowany'

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='notatki_notes',)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
                   ]
    def __str__(self):
        return self.title
## 46 podr