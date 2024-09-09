from django.contrib import admin
from .models import ContactMessage
from .models import AboutSection



@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'message', 'timestamp')
    search_fields = ('name', 'message')



admin.site.register(AboutSection)
