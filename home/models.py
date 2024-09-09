from django.db import models
from ckeditor.fields import RichTextField



# Create your models here.
# home/models.py

class ContactMessage(models.Model):
    name = models.CharField(max_length=100, default='Anonymous')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} at {self.timestamp}"

class AboutSection(models.Model):
    shorteducation = RichTextField()  # Brief info about education
    shortexperience = RichTextField()  # Brief info about experience
    shortpersonal = RichTextField()  # Brief info about personal interests

    def __str__(self):
        return "About Section Content"
