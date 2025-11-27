from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    
    title = models.CharField(max_length=30)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    slug = models.SlugField(unique=True, blank=True)
    
def save(self, *args, **kwargs):
    if not self.id:
        super().save(*args, **kwargs)
    if not self.slug:
        base_slug = slugify(self.title)
        self.slug = f"{base_slug}-{self.id}"
    super().save(*args, **kwargs)

    
    