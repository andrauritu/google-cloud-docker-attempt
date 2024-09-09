from django.shortcuts import render

def experience(request):
    return render(request, 'about/experience.html')

def education(request):
    return render(request, 'about/education.html')

def personal(request):
    return render(request, 'about/personal.html')
