# projects/views.py


from django.shortcuts import render, get_object_or_404
from .models import Project


def project_detail(request, slug):
    # Use get_object_or_404 to find the project by its slug
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'projects/detail.html', {'project': project})
