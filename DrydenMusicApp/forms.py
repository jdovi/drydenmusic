from django import forms
from .models import music
from django.contrib.auth.models import User

class EmailForm(forms.Form):

    SONG_OPTIONS = []
    m = music.objects.all()
    m = m.order_by('-added')
    for item in m:
        SONG_OPTIONS.append((item.id, item.title))

    EMAIL_OPTIONS = []
    u = User.objects.all()
    for item in u:
        EMAIL_OPTIONS.append((item.email, item.email))
    
    song_list = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                         choices=SONG_OPTIONS)
    email_list = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                         choices=EMAIL_OPTIONS)
