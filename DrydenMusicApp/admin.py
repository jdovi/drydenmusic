from django.contrib import admin
from .models import music

# Register your models here.

class MusicAdmin(admin.ModelAdmin):
    fields = ['title', 'first_line', 'music_file', 'file_type']


admin.site.register(music, MusicAdmin)
