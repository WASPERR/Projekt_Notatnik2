from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset() \
            .filter(status=Note.Status.PUBLISHED)
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
    status = models.CharField(max_length=12, choices=Status.choices, default=Status.DRAFT)
    object = models.Manager()
    published = PublishedManager()
    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
                   ]
    def __str__(self):
        return self.title
