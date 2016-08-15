from django.contrib import admin
from .models import music

# Register your models here.

class MusicAdmin(admin.ModelAdmin):
    fields = ['title', 'first_line', 'music_file']

admin.site.register(music, MusicAdmin)
