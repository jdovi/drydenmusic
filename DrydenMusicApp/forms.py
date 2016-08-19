from django import forms
from django.forms import ModelForm
from .models import music
from django.contrib.auth.models import User

import pdb

class EmailForm(forms.Form):

    song_list = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                         choices=[])
    email_list = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                         choices=[])
    
    #this allows the choice fields to be dynamically populated.
    def __init__(self,*args, **kwargs):
        super(EmailForm, self).__init__(*args, **kwargs)
        self.fields['song_list'].choices = [(x.pk, x.title) for x in music.objects.order_by('title')]
        self.fields['email_list'].choices = [(x.email, x.email) for x in User.objects.order_by('email')]

class UploadForm(ModelForm):
    class Meta:
        model = music
        fields = ['title','first_line','music_file','file_type']
        
