from django.shortcuts import render
from .models import EducationSection
from .models import ExperienceSection
from .models import PersonalSection




def education(request):
    sections = EducationSection.objects.all()  # Get all education sections
    return render(request, 'about/education.html', {'sections': sections})

def experience(request):
    sections = ExperienceSection.objects.all()  # Get all experience sections
    return render(request, 'about/experience.html', {'sections': sections})

def personal(request):
    sections = PersonalSection.objects.all()  # Get all personal sections
    return render(request, 'about/personal.html', {'sections': sections})