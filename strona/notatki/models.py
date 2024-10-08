from django.db import models
from django.utils import timezone

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at'])
                   ]
    def __str__(self):
        return self.title
## 46 podr