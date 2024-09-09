from django.urls import path
from . import views

app_name = 'about'

urlpatterns = [
    path('education/', views.education, name='education'),
    path('experience/', views.experience, name='experience'),
    path('personal/', views.personal, name='personal'),
]
