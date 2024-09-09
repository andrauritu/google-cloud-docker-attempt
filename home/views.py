from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import ContactMessage, AboutSection  # Import the AboutSection model
from projects.models import Project

def home(request):
    projects = Project.objects.all()  # Query all projects
    about_section = AboutSection.objects.first()  # Get the first (and only) AboutSection content

    # Handle form submission
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name', 'Anonymous')
            message = form.cleaned_data['message']

            # Save the message to the database
            ContactMessage.objects.create(name=name, message=message)

            # If it's an AJAX request, return JSON response instead of redirecting
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'message': 'Message sent successfully!'}, status=200)

            return redirect('/')  # Redirect for non-AJAX requests

    else:
        form = ContactForm()

    # Pass the AboutSection data, projects, and form to the template
    context = {
        'projects': projects,
        'form': form,
        'about_section': about_section,
    }

    return render(request, 'home.html', context)
