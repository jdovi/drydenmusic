from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as lgout
from django.shortcuts import render
from .models import music

# Create your views here.
@login_required
def index(request):
    latest_music_list = music.objects.order_by('added')
    context = {'latest_music_list': latest_music_list}
    return render(request, 'DrydenMusicApp/index.html', context)
    
def logout(request):
    lgout(request)
    return render(request,'registration/logout.html')
