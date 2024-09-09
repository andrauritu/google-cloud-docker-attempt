# home/forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=False, initial="Anonymous", max_length=100, label="Your Name")
    message = forms.CharField(widget=forms.Textarea, label="Your Message")


