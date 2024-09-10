from django.db import models
from ckeditor.fields import RichTextField  # For rich text fields

class EducationSection(models.Model):
    name = models.CharField(max_length=255)  # Required field
    extra1 = RichTextField(blank=True, null=True)  # Optional RichText
    image = models.ImageField(upload_to='education_images/', blank=True, null=True)  # Optional
    website = models.URLField(blank=True, null=True)  # Optional
    specialisation = models.CharField(max_length=255, blank=True, null=True)  # Optional
    gpa = models.CharField(max_length=10, blank=True, null=True)  # Optional
    relevant_subjects = RichTextField(blank=True, null=True)  # Optional RichText
    extra2 = RichTextField(blank=True, null=True)  # Optional RichText
    order = models.PositiveIntegerField(default=0)  # Field for ordering
    class Meta:
        ordering = ['order']  # Ensure sections are retrieved in order

    def __str__(self):
        return self.name


class ExperienceSection(models.Model):
    name = models.CharField(max_length=255)  # Required field
    description = RichTextField(blank=True, null=True)  # Optional RichText
    image = models.ImageField(upload_to='experience_images/', blank=True, null=True)  # Optional
    website = models.URLField(blank=True, null=True)  # Optional
    order = models.PositiveIntegerField(default=0)  # Field for ordering

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name
    
class PersonalSection(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)  # Optional
    description = RichTextField(blank=True, null=True)  # Optional RichText
    image1 = models.ImageField(upload_to='personal_images/', blank=True, null=True)  # Optional
    image2 = models.ImageField(upload_to='personal_images/', blank=True, null=True)  # Optional
    image3 = models.ImageField(upload_to='personal_images/', blank=True, null=True)  # Optional
    image4 = models.ImageField(upload_to='personal_images/', blank=True, null=True)  # Optional
    extra = RichTextField(blank=True, null=True)  # Optional RichText
    
    order = models.PositiveIntegerField(default=0)  # Field for ordering

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name