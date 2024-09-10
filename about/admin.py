from django.contrib import admin
from .models import EducationSection
from .models import ExperienceSection
from .models import PersonalSection

@admin.register(EducationSection)
class EducationSectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialisation', 'gpa', 'order')
    ordering = ('order',)  # Admin sorting

@admin.register(ExperienceSection)
class ExperienceSectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    ordering = ('order',)

@admin.register(PersonalSection)
class PersonalSectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    ordering = ('order',)
