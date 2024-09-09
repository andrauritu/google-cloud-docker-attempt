from django.db import models
from django.utils.text import slugify

from ckeditor.fields import RichTextField

class Project(models.Model):
    name = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, default="Not specified")  # Default value
    description = RichTextField()
    technologies = RichTextField()  # Default value
    date = models.DateField(default='2024-01-01')  # Already added date field with default
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

