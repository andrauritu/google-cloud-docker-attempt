from django.shortcuts import render, get_object_or_404
from .models import Project

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    
    # Split the technologies into a list and pass it to the template
    technologies = project.technologies.split(',')
    
    return render(request, 'projects/detail.html', {
        'project': project,
        'technologies': technologies
    })
