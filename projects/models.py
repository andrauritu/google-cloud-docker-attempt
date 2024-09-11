from django.db import models
from django.utils.text import slugify

from ckeditor.fields import RichTextField

class Project(models.Model):
    name = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, default="Not specified")  # Default value
    shortdescription = RichTextField( blank=True, null=True)
    technologies = RichTextField(blank=True, null=True)  # Default value
    date = models.CharField(max_length=100, default="Not specified")  # Default value
    longdescription = RichTextField(blank=True, null=True)
    website = models.URLField(max_length=200, blank=True, null=True)
    github = models.URLField(max_length=200, blank=True, null=True)
    mainimage = models.ImageField(upload_to="projects/images/", blank=True, null=True)
    youtubedemo = models.URLField(max_length=200, blank=True, null=True)
    extra1=RichTextField(blank=True, null=True)
    photo1 = models.ImageField(upload_to="projects/images/", blank=True, null=True)
    photo1caption = models.CharField(max_length=100, blank=True, null=True)
    photo2 = models.ImageField(upload_to="projects/images/", blank=True, null=True)
    photo2caption = models.CharField(max_length=100, blank=True, null=True)
    extra2=RichTextField(blank=True, null=True)
    photo3 = models.ImageField(upload_to="projects/images/", blank=True, null=True)
    photo3caption = models.CharField(max_length=100, blank=True, null=True)
    photo4 = models.ImageField(upload_to="projects/images/", blank=True, null=True)
    photo4caption = models.CharField(max_length=100, blank=True, null=True)
    extra3=RichTextField(blank=True, null=True)
    photo5 = models.ImageField(upload_to="projects/images/", blank=True, null=True)
    photo5caption = models.CharField(max_length=100, blank=True, null=True)
    photo6 = models.ImageField(upload_to="projects/images/", blank=True, null=True)
    photo6caption = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

